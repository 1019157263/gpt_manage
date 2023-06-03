from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from ui.Ui_main import Ui_MainWindow
import sys, os, json,requests
from digg_follow_no_tk import DouyinHighLevelAPI



class main_window(QMainWindow, Ui_MainWindow):
    # self.windowname=""
    def __init__(self):
        super().__init__()
        self.start_flg = True
        self.setupUi(self)
        self.congfigpath = "config.info"
        try:
            f = open(self.congfigpath,"r",encoding="utf-8").read()
            data =  json.loads(f)
            self.textEdit_2.setPlainText("\n".join(data["cookies_raw_list"]))#设置cookeis
            self.textEdit_3.setPlainText("\n".join(data["uid_list_raw_list"]))#设置cookeis
            self.textEdit.setPlainText(data["token"])#设置cookeis
            self.radioButton.setChecked(data["digg"])#设置cookeis
        except Exception as e:
            print(e)
            dic= {
            "cookies_raw_list":"",
            "uid_list_raw_list":"",
            "token":"",
            "digg":True
            }
            js = json.dumps(dic, sort_keys=True, indent=4,ensure_ascii=False ,separators=(',', ':'))
            f = open(self.congfigpath ,"w",encoding="utf-8")
            f.write(js)
            f.close()
            f = open(self.congfigpath,"r",encoding="utf-8").read()
            data =  json.loads(f)
            self.textEdit_2.setPlainText("\n".join(data["cookies_raw_list"]))#设置cookeis
            self.textEdit_3.setPlainText("\n".join(data["uid_list_raw_list"]))#设置cookeis
            self.textEdit.setPlainText(data["token"])#设置cookeis
            self.radioButton.setChecked(data["digg"])#设置cookeis


        print(data)
        self.pushButton.released.connect(self.outlinex)

    def closeEvent(self, event):
        print("关闭事件")
        self.closejob()

    def closejob(self):
        cookies_raw_list = self.textEdit_2.toPlainText().split("\n")
        uid_list_raw_list = self.textEdit_3.toPlainText().split("\n")
        token = self.textEdit.toPlainText()
        # self.textEdit.radioButton.isclicked()
        dic= {
            "cookies_raw_list":cookies_raw_list,
            "uid_list_raw_list":uid_list_raw_list,
            "token":token,
            "digg":self.radioButton.isChecked()
        }
        js = json.dumps(dic, sort_keys=True, indent=4,ensure_ascii=False ,separators=(',', ':'))
        f = open(self.congfigpath ,"w",encoding="utf-8")
        f.write(js)

    def outlinex(self):
        try:
            cookies_raw_list = self.textEdit_2.toPlainText().split("\n")
            uid_list_raw_list = self.textEdit_3.toPlainText().split("\n")
            token = self.textEdit.toPlainText()
            print(f"按下:{cookies_raw_list},{uid_list_raw_list}")
            for i in cookies_raw_list:
                job(cookies=i,uid_list=uid_list_raw_list,token_token=token,type_zz=self.radioButton.isChecked())
        except Exception as E:
            print(f"错误:{E}")


def job(cookies,uid_list,token_token,type_zz=0,):
    print(cookies)
    print(type_zz)
    douyin = DouyinHighLevelAPI(cookies,token_token)
    for i in uid_list: 
        douyin.digg(i)
    # del douyin

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MianWindow = main_window()
    MianWindow.show()
    sys.exit(app.exec_())





'''
ttwid=1%7CJwEWlAiaGoGS6-81RbiP57snFHf10HNGPuxomIRo6NM%7C1625226422%7C60a687cdd94c533a28fd0f30ae4d4024bfcc918feb0f63922254fc6597969d96; sessionid_ss=cf37bc2390a2469dc1ae2c1e2586519e
ttwid=1%7CJwEWlAiaGoGS6-81RbiP57snFHf10HNGPuxomIRo6NM%7C1625226422%7C60a687cdd94c533a28fd0f30ae4d4024bfcc918feb0f63922254fc6597969d96; sessionid_ss=cf37bc2390a2469dc1ae2c1e2586519e
#"ttwid=1%7CJwEWlAiaGoGS6-81RbiP57snFHf10HNGPuxomIRo6NM%7C1625226422%7C60a687cdd94c533a28fd0f30ae4d4024bfcc918feb0f63922254fc6597969d96; sessionid_ss=cf37bc2390a2469dc1ae2c1e2586519e"
# "b153c6e814f4601759b28206bfa6e469"
# 6986854475470277924
# 6947627772302986533
'''
