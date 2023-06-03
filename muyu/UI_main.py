from re import S, split
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from Ui_UI import Ui_MainWindow

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


import sys, os, json,requests
# from digg_follow_no_tk import DouyinHighLevelAPI
import main
import time
import  threading
'''
1.读取配置
2.配置ui
3.读取ui
4.开始运行

'''
ISSTAR =True

class pppprint:
    def __init__(self,ui):
        self.ui = ui
    def write(self,strx):
        self.ui.append(strx.replace("\n\n","\n"))
        self.ui.moveCursor(self.ui.textCursor().End) # 文本框显示到底部




jobs_list = []

def jobthread():
    print(f"[线程启动成功]")
    while True:
        for douyin in jobs_list:
            try:
                time.sleep(1)
                if(not ISSTAR):
                    print("已停止",end="\r")
                    continue
                # print(douyin)
                print(f"[账号]：{douyin.uid},做关注任务")
                JOB = douyin.doguanzhu("")
                retpor = JOB["response"]
                print(retpor)
                guanzhuok =True
                if ("关注太快" in str(retpor)):
                    print("关注太快，已上限了？")
                    guanzhuok = False
                if(JOB["raw_job"]["msg"] != "没可做任务了" and guanzhuok):
                    dy_task_log_id = JOB["raw_job"]["data"]["dy_task_log_id"]
                    print(douyin.puttask(dy_task_log_id,"协议"))
                guanzhuok =True

                
                
                print("关注任务结束")
                time.sleep(1)
                print("做点赞任务")
                print(f"[账号]：{douyin.uid},做点赞任务")
                JOB = douyin.dodianzhan("")
                print("点赞任务结束")
                if(JOB["raw_job"]["msg"] != "没可做任务了" ):
                    dy_task_log_id = JOB["raw_job"]["data"]["dy_task_log_id"]
                    # A.puttask(JOB)
                    print(douyin.puttask(dy_task_log_id,"协议"))
            except Exception as e:
                print("[错误]"+str(e))
class Example(QThread):

    def __init__(self):
        super().__init__()

    def __del__(self):
        self.wait()

    def run(self):
        jobthread()


        # 进行任务操作
        # self.signal.emit()    # 发射信号
class main_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.isstart = False
        self.isone = True
        super().__init__()
        self.start_flg = True
        self.setupUi(self)
        self.token_ui = self.lineEdit
        self.cookies_ui = self.plainTextEdit
        # self.log_ui = self.textBrowser
        self.configpath = "config.json"
        config = self.getConfig()
        self.token_ui.setText(config["muyutoken"])
        self.cookies_ui.setPlainText(config["cookies"])
        self.pushButton.released.connect(self.outlinex)

        # sys.stdout = pppprint(self.log_ui)

    def outlinex(self):
        global ISSTAR
        print(f"点击成功:{not self.isstart}",end="")

        ISSTAR =  not self.isstart
        self.isstart = not self.isstart
        self.pushButton.setText("停止" if self.isstart else "开始")
        self.label_3.setText("状态：运行中..." if self.isstart else "状态：暂停中...")
        self.job()
    


    def job(self):
        global jobs_list
        if (self.isone):
            print("开始装载")
            self.jobs_list = []
            for i in self.cookies_ui.toPlainText().split("\n"):
                A =main.muyuAPI(i,self.token_ui.text())
                self.jobs_list.append(A)
                # print(A)
            jobs_list = self.jobs_list
            print("装载完成")
            self.isone=False
            self.thread = Example()
            # self.thread.signal.connect(self.callback)
            self.thread.start()    # 启动线程
            #启动任务线程
            # t = _thread.start_new_thread(jobthread  (self, ))
            print("线程启动成功")
            
        
        
    def closeEvent(self, event):
        print("关闭事件")
        self.closejob()
    def closejob(self):
        config = {
            "muyutoken":self.token_ui.text(),
            "cookies":self.cookies_ui.toPlainText()
        }
        F = open(self.configpath,"w",encoding="utf-8")
        js = json.dumps(config, sort_keys=True, indent=4,ensure_ascii=False ,separators=(',', ':'))
        F.write(js)

    def getConfig(self):
        config = {
            "muyutoken":"",
            "cookies":""
        }
        try:
            with open(self.configpath,"r",encoding="utf-8") as F:
                config_raw = F.read()
            config = json.loads(config_raw)
            return config
        except:
            print("第一次使用")
            F = open(self.configpath,"w",encoding="utf-8")
            js = json.dumps(config, sort_keys=True, indent=4,ensure_ascii=False ,separators=(',', ':'))
            F.write(js)
            return config


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MianWindow = main_window()
    MianWindow.show()
    sys.exit(app.exec_())



# name = "boob"
# age = 12

# print(f"name:{name},age:{age}")