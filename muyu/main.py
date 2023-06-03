from datetime import date
from typing import Text
import requests,time,json
from requests.api import head, post
from digg_follow_no_tk import DouyinHighLevelAPI
import os

from email.mime.text import MIMEText
import smtplib



YOUJIAN = 0

def faemeil(xxx='默认'):
    global YOUJIAN
    if(time.time()- YOUJIAN >=60*10):
        subject = "抖音收益出现验证码通知"
        content = f"<h4>{xxx}</h4>"  # 邮件内容
        sender = "18381801393@163.com"  # 发件人
        password = "FZMGTDSHPHARIYAI" # 刚才我们在163邮箱里设置的授权密码
        receivers = ["1019157263@qq.com"]  # 收件人
        for receiver in receivers:
            message = MIMEText(content, "html", "utf-8")
            message["From"] = "抖音收益出现验证码通知"
            message["To"] = receiver
            message["Subject"] = subject
            
            smtp = smtplib.SMTP_SSL('smtp.163.com', 994)
            smtp.login(sender, password)
            smtp.sendmail(sender, [receiver], message.as_string())
            smtp.close()
        YOUJIAN = time.time()
    else:
        print("邮件发的太快了。。已经发过了")


URL = "http://127.0.0.1:8000/"
def log(mse,users,state):
    data={
        "mse":json.dumps(mse),
        "users":users,
        "state":state
    }
    url = URL+"token/log"
    req = requests.post(url,data=data)
    print(req.json())
class muyuAPI:
    def __del__(self):
        print(self.li_not_ok)
    def __init__(self,cookies,muyutoken):
        #错误记录，达到10次错误，等待20分钟，再清零重试
        #点赞数量

        self.err = {
            "总":[0,True,time.time()],
            "2":[0,True,time.time()],#点赞
            "1":[0,True,time.time()] #关注
        }

        self.li_not_ok = []
        self.session = requests.session()
        self.singe_token = "b153c6e814f4601759b28206bfa6e469"
        hea= {
            "token":muyutoken
        }
        self.session.headers.update(hea)
        #cookies参数要齐全，失败后需要去网页做一下验证
        self.cookies_xxx = cookies
        self.douyinapi = DouyinHighLevelAPI(self.cookies_xxx,self.singe_token)
        self.uid = self.douyinapi.uid
        
        # self.douyinapi = DouyinHighLevelAPI("ttwid=1%7CEEQ9p2-iPJjG_njJqxJDLZOGKtRKWDJ3IpdAMftyH0Q%7C1629168134%7Ca6e55daa011a4694c44d346109b47476823d16c3e2e521fb98f7239358a2c472; passport_csrf_token_default=a03df3ac2f0aef315ad9d33b0916cd42; passport_csrf_token=a03df3ac2f0aef315ad9d33b0916cd42; n_mh=vYrW8M90nu-LD-hIJEMs1QvY2Pc6XEVeY9oEF5zUgOs; sso_uid_tt=04332b5b4937523e2c8e97029f7e19f4; sso_uid_tt_ss=04332b5b4937523e2c8e97029f7e19f4; toutiao_sso_user=2efed3be8fa6b75c715909bb71107e05; toutiao_sso_user_ss=2efed3be8fa6b75c715909bb71107e05; odin_tt=26ad6dedcf4df42be5626ebf207e4127cd7cb289e030fb56deed02bc5d901e93619e61681be7075dab4d2f196e8b4927a1a9978fd403459e094fb12ccc338dd9; passport_auth_status_ss=59e448ef2b8657ba73871420feeec18f%2C; sid_guard=2522f3210fc6a6a1b4bf951ef5c33a87%7C1629168451%7C5183999%7CSat%2C+16-Oct-2021+02%3A47%3A30+GMT; uid_tt=39aa60150b029633e32dec0fe5fbf267; uid_tt_ss=39aa60150b029633e32dec0fe5fbf267; sid_tt=2522f3210fc6a6a1b4bf951ef5c33a87; sessionid=2522f3210fc6a6a1b4bf951ef5c33a87; sessionid_ss=2522f3210fc6a6a1b4bf951ef5c33a87; sid_ucp_v1=1.0.0-KDg4MDIyYTc4ZDdjZWM1MTVlMWRmODQxNmI2ZjNiNDQ5ZDkzMzI3YTIKFQjquMXv-wIQw8bsiAYY7zE4BkD0BxoCbGYiIDI1MjJmMzIxMGZjNmE2YTFiNGJmOTUxZWY1YzMzYTg3; ssid_ucp_v1=1.0.0-KDg4MDIyYTc4ZDdjZWM1MTVlMWRmODQxNmI2ZjNiNDQ5ZDkzMzI3YTIKFQjquMXv-wIQw8bsiAYY7zE4BkD0BxoCbGYiIDI1MjJmMzIxMGZjNmE2YTFiNGJmOTUxZWY1YzMzYTg3; passport_auth_status=59e448ef2b8657ba73871420feeec18f%2C; s_v_web_id=verify_ksmo91lv_IV8PEuYk_Oj2M_4CTi_8ee1_OtrW2xA8aPeU; csrf_session_id=358124a1bed349939d72753463a63df4; MONITOR_WEB_ID=b4f69576-e1cd-44a0-8e0b-356434bb5a4b",self.singe_token)

        # self.douyinapi = DouyinHighLevelAPI("ttwid=1%7CEEQ9p2-iPJjG_njJqxJDLZOGKtRKWDJ3IpdAMftyH0Q%7C1629168134%7Ca6e55daa011a4694c44d346109b47476823d16c3e2e521fb98f7239358a2c472; passport_csrf_token_default=a03df3ac2f0aef315ad9d33b0916cd42; passport_csrf_token=a03df3ac2f0aef315ad9d33b0916cd42; n_mh=vYrW8M90nu-LD-hIJEMs1QvY2Pc6XEVeY9oEF5zUgOs; sso_uid_tt=04332b5b4937523e2c8e97029f7e19f4; sso_uid_tt_ss=04332b5b4937523e2c8e97029f7e19f4; toutiao_sso_user=2efed3be8fa6b75c715909bb71107e05; toutiao_sso_user_ss=2efed3be8fa6b75c715909bb71107e05; odin_tt=26ad6dedcf4df42be5626ebf207e4127cd7cb289e030fb56deed02bc5d901e93619e61681be7075dab4d2f196e8b4927a1a9978fd403459e094fb12ccc338dd9; passport_auth_status_ss=59e448ef2b8657ba73871420feeec18f%2C; sid_guard=2522f3210fc6a6a1b4bf951ef5c33a87%7C1629168451%7C5183999%7CSat%2C+16-Oct-2021+02%3A47%3A30+GMT; uid_tt=39aa60150b029633e32dec0fe5fbf267; uid_tt_ss=39aa60150b029633e32dec0fe5fbf267; sid_tt=2522f3210fc6a6a1b4bf951ef5c33a87; sessionid=2522f3210fc6a6a1b4bf951ef5c33a87; sessionid_ss=2522f3210fc6a6a1b4bf951ef5c33a87; sid_ucp_v1=1.0.0-KDg4MDIyYTc4ZDdjZWM1MTVlMWRmODQxNmI2ZjNiNDQ5ZDkzMzI3YTIKFQjquMXv-wIQw8bsiAYY7zE4BkD0BxoCbGYiIDI1MjJmMzIxMGZjNmE2YTFiNGJmOTUxZWY1YzMzYTg3; ssid_ucp_v1=1.0.0-KDg4MDIyYTc4ZDdjZWM1MTVlMWRmODQxNmI2ZjNiNDQ5ZDkzMzI3YTIKFQjquMXv-wIQw8bsiAYY7zE4BkD0BxoCbGYiIDI1MjJmMzIxMGZjNmE2YTFiNGJmOTUxZWY1YzMzYTg3; passport_auth_status=59e448ef2b8657ba73871420feeec18f%2C; s_v_web_id=verify_ksmo91lv_IV8PEuYk_Oj2M_4CTi_8ee1_OtrW2xA8aPeU; csrf_session_id=358124a1bed349939d72753463a63df4; douyin.com; MONITOR_WEB_ID=b4f69576-e1cd-44a0-8e0b-356434bb5a4b",self.singe_token)

    def setAPI(self,cookies):
        # del self.session
        self.session=DouyinHighLevelAPI(cookies,self.singe_token)
    def login(self):
        url="http://muyu.doudouqwe.com/api/app/user/login"
        data = {
            "username": "18381801393",
            "password": "a1019157263"
        }
        login_raw=self.session.post(url=url,data=data).json()
        return login_raw["data"]["userinfo"]["token"]
    def puttask(self,dy_task_log_id,file_url):
        url = f"http://muyu.doudouqwe.com/api/app/dy_task_logc/submit?dy_task_log_id={dy_task_log_id}&file_url={file_url}"
        raw_req = self.session.get(url)
        return raw_req.text
    def dotask(self,type_s):
        url = "http://muyu.doudouqwe.com/api/app/dy_taskc/getone"
        data_x = {
            "types": type_s,#2点赞.1关注
            "xpwiok_uid": int(self.douyinapi.get_user_id())
        }
        print(data_x)
        onetask = self.session.post(url=url,data=data_x).json()
        print(onetask)
        if(onetask["msg"] != "没可做任务了"):
            if (data_x["types"] == 1):#关注
                ret = self.doguanzhu(onetask)
                job={
                    "types":data_x["types"],
                    "raw_job":onetask,
                    "response":ret 
                        }
                return job
            if (data_x["types"]  == 2):#点赞
                ret = self.dodianzhan(onetask)
                job={
                    "types":data_x["types"],
                    "raw_job":onetask,
                    "response":ret 
                        }
                return job
        else:
            job={
                    "types":data_x["types"],
                    "raw_job":onetask,
                    "response":"没有任务可做了" 
                        }
            return job

    def doguanzhu(self,ret):#关注
        url = "http://muyu.doudouqwe.com/api/app/dy_taskc/getone"
        data_x = {
            "types": 1,#2点赞.1关注
            "xpwiok_uid": int(self.douyinapi.get_user_id())
        }
        print(data_x)
        onetask = self.session.post(url=url,data=data_x).json()
        print(onetask)
        if  (onetask["msg"] != "没可做任务了"):
            userid = onetask["data"]["author_user_id"]
            print(userid)
            req_ret = self.douyinapi.follow(user_id=userid).json()#关注
            if("is_enterprise" not in req_ret.keys()):
                print("关注失败,可能是出验证码了")
                faemeil(f"抖音出现了验证码，快去看看吧！<br>响应：{req_ret}")

                #发邮件
            job={
                "types":data_x["types"],
                "raw_job":onetask,
                "response":req_ret 
            }
            return job
        else:
            job={
                "types":data_x["types"],
                "raw_job":onetask,
                "response":"没可做任务了" 
            }
            return job
    def dodianzhan(self,ret):#点赞
        url = "http://muyu.doudouqwe.com/api/app/dy_taskc/getone"
        data_x = {
            "types": 2,#2点赞.1关注
            "xpwiok_uid": int(self.douyinapi.get_user_id())
        }
        print(data_x)
        onetask = self.session.post(url=url,data=data_x).json()
        print(onetask)
        if  (onetask["msg"] != "没可做任务了"):
            video_id = onetask["data"]["copyUrl"].split("/")[-1]
            print(video_id)
            req_ret = self.douyinapi.digg(aweme_id=video_id).json()
            job={
                "types":data_x["types"],
                "raw_job":onetask,
                "response":req_ret 
            }
            return job
        else: 
            job={
                "types":data_x["types"],
                "raw_job":onetask,
                "response":"没可做任务了" 
            }
            return job
    def getonetask(self,type_s="1"):
        print(f"累计错误:{self.err}")
        url = "http://muyu.doudouqwe.com/api/app/dy_taskc/getone"
        data = {
            "types": type_s,#2点赞.1关注
            "xpwiok_uid": self.douyinapi.get_user_id()
        }
        print(data)
        try:
            if(data["types"]=="2" and self.err["2"][1] ):#点赞开关
                #点赞
                onetask = self.session.post(url=url,data=data).json()
                print(onetask)

                if(onetask["mse"] != "没可做任务了"):
                    video_id = onetask["data"]["copyUrl"].split("/")[-1]
                    print(video_id)
                    req_ret = self.douyinapi.digg(aweme_id=video_id).json()
                    job={
                            "types":data["types"],
                            "raw_job":onetask,
                            "response":req_ret
                        }
                    if (req_ret["is_digg"]==1):
                        self.err["2"][0] +=1
                        print("点赞失败，已加入列表")
                        log(mse=job,users=self.singe_token,state="[点赞任务]失败")
                        # self.li_not_ok.append(job)
                        return False
                    else:
                        log(mse=job,users=self.singe_token,state="[点赞任务]成功")
                else:
                    job={
                            "types":data["types"],
                            "raw_job":onetask,
                            "response":"没任务可做了"
                        }
                return job
            if(self.err["2"][0]>10):
                self.err["2"][1] =False#关闭点赞开关
            if(not self.err["2"][1] and (time.time() - self.err["2"][2])>60*ti ):#打开点赞开关
                #已有10分钟，打开开关
                self.err["2"][0]  = 0
                self.err["2"][1]  = True
            if(self.err["1"][0]>10):
                self.err["1"][1] =False#关闭关注开关
            if(not self.err["1"][1] and (time.time() - self.err["1"][2])>60*ti ):#打开关注开关
                #已有10分钟，打开开关
                self.err["1"][0]  = 0
                self.err["1"][1]  = True
            if(data["types"]=="1" and self.err["1"][1] ):#关注开关
                #关注
                onetask = self.session.post(url=url,data=data).json()   
                print(onetask)
                
                userid = onetask["data"]["author_user_id"]
                print(userid)
                req_ret = self.douyinapi.follow(user_id=userid).json()#关注
                job={
                        "types":data["types"],
                        "raw_job":onetask,
                        "response":req_ret
                    }
                if("is_enterprise" in req_ret.keys()):
                    log(mse=job,users=self.singe_token,state="[关注任务]成功")
                    return job
                else:
                    print("关注失败，已加入列表")
                    log(mse=job,users=self.singe_token,state="[关注任务]失败")
                    # self.li_not_ok.append(job)
                    return False
        except Exception as e:
            print(e)
            return False
        # print(onetask)

# def sleep_x(n):
#     for i in range(n):
#         time.sleep(1)

'''
ttwid=1%7CEEQ9p2-iPJjG_njJqxJDLZOGKtRKWDJ3IpdAMftyH0Q%7C1629168134%7Ca6e55daa011a4694c44d346109b47476823d16c3e2e521fb98f7239358a2c472; passport_csrf_token_default=a03df3ac2f0aef315ad9d33b0916cd42; passport_csrf_token=a03df3ac2f0aef315ad9d33b0916cd42; n_mh=vYrW8M90nu-LD-hIJEMs1QvY2Pc6XEVeY9oEF5zUgOs; sso_uid_tt=04332b5b4937523e2c8e97029f7e19f4; sso_uid_tt_ss=04332b5b4937523e2c8e97029f7e19f4; toutiao_sso_user=2efed3be8fa6b75c715909bb71107e05; toutiao_sso_user_ss=2efed3be8fa6b75c715909bb71107e05; odin_tt=26ad6dedcf4df42be5626ebf207e4127cd7cb289e030fb56deed02bc5d901e93619e61681be7075dab4d2f196e8b4927a1a9978fd403459e094fb12ccc338dd9; passport_auth_status_ss=59e448ef2b8657ba73871420feeec18f%2C; sid_guard=2522f3210fc6a6a1b4bf951ef5c33a87%7C1629168451%7C5183999%7CSat%2C+16-Oct-2021+02%3A47%3A30+GMT; uid_tt=39aa60150b029633e32dec0fe5fbf267; uid_tt_ss=39aa60150b029633e32dec0fe5fbf267; sid_tt=2522f3210fc6a6a1b4bf951ef5c33a87; sessionid=2522f3210fc6a6a1b4bf951ef5c33a87; sessionid_ss=2522f3210fc6a6a1b4bf951ef5c33a87; sid_ucp_v1=1.0.0-KDg4MDIyYTc4ZDdjZWM1MTVlMWRmODQxNmI2ZjNiNDQ5ZDkzMzI3YTIKFQjquMXv-wIQw8bsiAYY7zE4BkD0BxoCbGYiIDI1MjJmMzIxMGZjNmE2YTFiNGJmOTUxZWY1YzMzYTg3; ssid_ucp_v1=1.0.0-KDg4MDIyYTc4ZDdjZWM1MTVlMWRmODQxNmI2ZjNiNDQ5ZDkzMzI3YTIKFQjquMXv-wIQw8bsiAYY7zE4BkD0BxoCbGYiIDI1MjJmMzIxMGZjNmE2YTFiNGJmOTUxZWY1YzMzYTg3; passport_auth_status=59e448ef2b8657ba73871420feeec18f%2C; douyin.com; csrf_session_id=0c8ffda4ce5240419bc3c72120c907c1; s_v_web_id=verify_f5b4b75f9a3c3bcae875cee47124a4e6; MONITOR_WEB_ID=b4f69576-e1cd-44a0-8e0b-356434bb5a4b
ttwid=1%7CEEQ9p2-iPJjG_njJqxJDLZOGKtRKWDJ3IpdAMftyH0Q%7C1629168134%7Ca6e55daa011a4694c44d346109b47476823d16c3e2e521fb98f7239358a2c472; passport_csrf_token_default=a03df3ac2f0aef315ad9d33b0916cd42; passport_csrf_token=a03df3ac2f0aef315ad9d33b0916cd42; n_mh=vYrW8M90nu-LD-hIJEMs1QvY2Pc6XEVeY9oEF5zUgOs; sso_uid_tt=04332b5b4937523e2c8e97029f7e19f4; sso_uid_tt_ss=04332b5b4937523e2c8e97029f7e19f4; toutiao_sso_user=2efed3be8fa6b75c715909bb71107e05; toutiao_sso_user_ss=2efed3be8fa6b75c715909bb71107e05; odin_tt=26ad6dedcf4df42be5626ebf207e4127cd7cb289e030fb56deed02bc5d901e93619e61681be7075dab4d2f196e8b4927a1a9978fd403459e094fb12ccc338dd9; passport_auth_status_ss=59e448ef2b8657ba73871420feeec18f%2C; sid_guard=2522f3210fc6a6a1b4bf951ef5c33a87%7C1629168451%7C5183999%7CSat%2C+16-Oct-2021+02%3A47%3A30+GMT; uid_tt=39aa60150b029633e32dec0fe5fbf267; uid_tt_ss=39aa60150b029633e32dec0fe5fbf267; sid_tt=2522f3210fc6a6a1b4bf951ef5c33a87; sessionid=2522f3210fc6a6a1b4bf951ef5c33a87; sessionid_ss=2522f3210fc6a6a1b4bf951ef5c33a87; sid_ucp_v1=1.0.0-KDg4MDIyYTc4ZDdjZWM1MTVlMWRmODQxNmI2ZjNiNDQ5ZDkzMzI3YTIKFQjquMXv-wIQw8bsiAYY7zE4BkD0BxoCbGYiIDI1MjJmMzIxMGZjNmE2YTFiNGJmOTUxZWY1YzMzYTg3; ssid_ucp_v1=1.0.0-KDg4MDIyYTc4ZDdjZWM1MTVlMWRmODQxNmI2ZjNiNDQ5ZDkzMzI3YTIKFQjquMXv-wIQw8bsiAYY7zE4BkD0BxoCbGYiIDI1MjJmMzIxMGZjNmE2YTFiNGJmOTUxZWY1YzMzYTg3; passport_auth_status=59e448ef2b8657ba73871420feeec18f%2C; douyin.com; csrf_session_id=aaab6081f9734c2d96e619bc8dbdc718; s_v_web_id=verify_8f27b831e5cf207da064d3f624dd4695; MONITOR_WEB_ID=b4f69576-e1cd-44a0-8e0b-356434bb5a4b"

'''

if __name__ == "__main__" :

    A = muyuAPI("ttwid=1%7CEEQ9p2-iPJjG_njJqxJDLZOGKtRKWDJ3IpdAMftyH0Q%7C1629168134%7Ca6e55daa011a4694c44d346109b47476823d16c3e2e521fb98f7239358a2c472; passport_csrf_token_default=a03df3ac2f0aef315ad9d33b0916cd42; passport_csrf_token=a03df3ac2f0aef315ad9d33b0916cd42; n_mh=vYrW8M90nu-LD-hIJEMs1QvY2Pc6XEVeY9oEF5zUgOs; sso_uid_tt=04332b5b4937523e2c8e97029f7e19f4; sso_uid_tt_ss=04332b5b4937523e2c8e97029f7e19f4; toutiao_sso_user=2efed3be8fa6b75c715909bb71107e05; toutiao_sso_user_ss=2efed3be8fa6b75c715909bb71107e05; odin_tt=26ad6dedcf4df42be5626ebf207e4127cd7cb289e030fb56deed02bc5d901e93619e61681be7075dab4d2f196e8b4927a1a9978fd403459e094fb12ccc338dd9; passport_auth_status_ss=59e448ef2b8657ba73871420feeec18f%2C; sid_guard=2522f3210fc6a6a1b4bf951ef5c33a87%7C1629168451%7C5183999%7CSat%2C+16-Oct-2021+02%3A47%3A30+GMT; uid_tt=39aa60150b029633e32dec0fe5fbf267; uid_tt_ss=39aa60150b029633e32dec0fe5fbf267; sid_tt=2522f3210fc6a6a1b4bf951ef5c33a87; sessionid=2522f3210fc6a6a1b4bf951ef5c33a87; sessionid_ss=2522f3210fc6a6a1b4bf951ef5c33a87; sid_ucp_v1=1.0.0-KDg4MDIyYTc4ZDdjZWM1MTVlMWRmODQxNmI2ZjNiNDQ5ZDkzMzI3YTIKFQjquMXv-wIQw8bsiAYY7zE4BkD0BxoCbGYiIDI1MjJmMzIxMGZjNmE2YTFiNGJmOTUxZWY1YzMzYTg3; ssid_ucp_v1=1.0.0-KDg4MDIyYTc4ZDdjZWM1MTVlMWRmODQxNmI2ZjNiNDQ5ZDkzMzI3YTIKFQjquMXv-wIQw8bsiAYY7zE4BkD0BxoCbGYiIDI1MjJmMzIxMGZjNmE2YTFiNGJmOTUxZWY1YzMzYTg3; passport_auth_status=59e448ef2b8657ba73871420feeec18f%2C; douyin.com; csrf_session_id=aaab6081f9734c2d96e619bc8dbdc718; s_v_web_id=verify_8f27b831e5cf207da064d3f624dd4695; MONITOR_WEB_ID=b4f69576-e1cd-44a0-8e0b-356434bb5a4b","8ea905dd-b03d-40e6-aac0-ce4350b762d0")
    for i in range(10000000):
        time.sleep(1)

        JOB = A.doguanzhu("")
        retpor = JOB["response"]
        print(retpor)
        guanzhuok =True
        if ("关注太快" in str(retpor)):
            print("关注太快，已上限了？")
            guanzhuok = False

        if(JOB["raw_job"]["msg"] != "没可做任务了" and guanzhuok):
            dy_task_log_id = JOB["raw_job"]["data"]["dy_task_log_id"]
            print(A.puttask(dy_task_log_id,"协议"))
        guanzhuok =True
        print("关注任务结束")
        

        time.sleep(1)
        
        print("做点赞任务")
        JOB = A.dodianzhan("")
        print("点赞任务结束")

        if(JOB["raw_job"]["msg"] != "没可做任务了" ):
            dy_task_log_id = JOB["raw_job"]["data"]["dy_task_log_id"]
            # A.puttask(JOB)
            print(A.puttask(dy_task_log_id,"协议"))



























'''
成功：
{'log_pb': {'impr_id': '202108241756320102111940474D01B14E'}, 'status_code': 0, 'status_msg': '', 'follow_status': 1, 'is_enterprise': 0, 'footer': {'show_entrance': 0, 'text': '', 'type': 0, 'duration': 0}, 'extra': {'logid': '202108241756320102111940474D01B14E', 'now': 1629798992000, 'fatal_item_ids': []}}
验证码：
{'status_code': 0, 'status_msg': '', 'follow_status': 1, 'is_enterprise': 1, 'footer': {'show_entrance': 0, 'text': '', 'type': 0, 'duration': 0}, 'extra': {'now': 1629799015000, 'fatal_item_ids': [], 'logid': '202108241756550102120420323501E556'}, 'log_pb': {'impr_id': '202108241756550102120420323501E556'}}

{'status_code': 0, 'follow_status': 1, 'extra': {'now': 1629808977000, 'fatal_item_ids': [], 'logid': '202108242042570102120991964310375A'}, 'log_pb': {'impr_id': '202108242042570102120991964310375A'}}

{'status_code': 2149, 'status_msg': '关注太快了，先休息一下吧～', 'log_pb': {'impr_id': '202108251046470102121681030B24F891'}}
'''


    # A.setAPI("ttwid=1%7CGryCFE1N45WnOqqUwEmiC7xOpkPiCBNBAtVf4sorLqk%7C1629378995%7C8470b7d4bb816a6c0ef69ac779749108c1aec9f1343c2f63876a56602da3663a; douyin.com; passport_csrf_token_default=a29362dd53580eefab881d99d75da818; passport_csrf_token=a29362dd53580eefab881d99d75da818; s_v_web_id=verify_ksiy6ryj_ZDqhFEOy_agUn_4RJr_BQJw_hUHWriliknAL; n_mh=9-mIeuD4wZnlYrrOvfzG3MuT6aQmCUtmr8FxV8Kl8xY; sso_uid_tt=4ffa4d80f274ac4406c6b028c325a133; sso_uid_tt_ss=4ffa4d80f274ac4406c6b028c325a133; toutiao_sso_user=4fcb6f60421f5803f61571e57bbb3b8f; toutiao_sso_user_ss=4fcb6f60421f5803f61571e57bbb3b8f; odin_tt=416a0365cdfce16ee0f5fedb3be36f5ce2b450d3aa47347c085cbdc555efd7eaf2c8e7112299a1bedc10ec7966c1bbb89aebfa360ba82ff55048bb770c3117a7; passport_auth_status_ss=21ea276df0826cf2d69c96e3546f17d8%2C; sid_guard=6f3b58ce93d0ecfe7d0b587d252f8b12%7C1629379365%7C5183999%7CMon%2C+18-Oct-2021+13%3A22%3A44+GMT; uid_tt=0f85f8ce96dfe423b3e2b19af825007f; uid_tt_ss=0f85f8ce96dfe423b3e2b19af825007f; sid_tt=6f3b58ce93d0ecfe7d0b587d252f8b12; sessionid=6f3b58ce93d0ecfe7d0b587d252f8b12; sessionid_ss=6f3b58ce93d0ecfe7d0b587d252f8b12; sid_ucp_v1=1.0.0-KDM5NmVhNWEzYTY5YWM5YmIyNjc3ZmJjMjIyMjc0NGI2ODk4MjE3MGEKFwjH_uD16Y3AARCltvmIBhjvMTgGQPQHGgJsZiIgNmYzYjU4Y2U5M2QwZWNmZTdkMGI1ODdkMjUyZjhiMTI; ssid_ucp_v1=1.0.0-KDM5NmVhNWEzYTY5YWM5YmIyNjc3ZmJjMjIyMjc0NGI2ODk4MjE3MGEKFwjH_uD16Y3AARCltvmIBhjvMTgGQPQHGgJsZiIgNmYzYjU4Y2U5M2QwZWNmZTdkMGI1ODdkMjUyZjhiMTI; passport_auth_status=21ea276df0826cf2d69c96e3546f17d8%2C; MONITOR_WEB_ID=d55f9a0a-12f8-4089-8089-87dc23de94c2")
    # for i in range(100000):
    #     print(A.err)
    #     time.sleep(1)
    #     if(not A.err["总"][1]):
    #         print(f"总共失败10次，暂停10分钟:{A.err}")
    #     if(A.err["总"][1]):#总开关
    #         print("领取关注任务")

    #         job = A.getonetask(type_s="1")#关注c

    #         if (job != False):
    #             if(job["raw_job"]["msg"] != "没有可做任务了"):
    #                 dy_task_log_id = job["raw_job"]["data"]["dy_task_log_id"]
    #                 file_url = "协议，不知道提交什么。问你们客服又不回，麻烦联系我。"
    #                 req = A.puttask(dy_task_log_id=dy_task_log_id,file_url=file_url)
    #                 print(req.text)
    #             else:
    #                 print("没有可做任务了")
    #         else:
    #             A.err["总"][0]+=1
    #             if(A.err["总"][0]>10):
    #                 A.err["总"][1] = False #暂停任务
    #                 A.err["总"][2] = time.time()#计时开始
    #             print("出错，放弃任务")


    #         time.sleep(1)
    #         print("领取点赞任务")
    #         job = A.getonetask(type_s="2")#点赞c
    #         if (job != False):
    #             if(job["raw_job"]["msg"] != "没有可做任务了"):
    #                 dy_task_log_id = job["raw_job"]["data"]["dy_task_log_id"]
    #                 file_url = "协议"
    #                 req = A.puttask(dy_task_log_id=dy_task_log_id,file_url=file_url)
    #                 print(req.text)
    #             else:
    #                 print("没有可做任务了")
    #         else:
    #             A.err["2"][0]+=1
    #             if(A.err["2"][0]>10):
    #                 A.err["2"][1] = False #暂停任务
    #                 A.err["2"][2] = time.time()#计时开始
    #             print("出错，放弃任务")

    #     elif(not A.err["总"][1] and (time.time()-A.err["总"][2])>60*ti ):
    #         #已有10分钟，打开开关
    #         A.err["总"][0]  = 0
    #         A.err["总"][1]  = True
















'''
老板
ttwid=1%7CEEQ9p2-iPJjG_njJqxJDLZOGKtRKWDJ3IpdAMftyH0Q%7C1629168134%7Ca6e55daa011a4694c44d346109b47476823d16c3e2e521fb98f7239358a2c472; passport_csrf_token_default=a03df3ac2f0aef315ad9d33b0916cd42; passport_csrf_token=a03df3ac2f0aef315ad9d33b0916cd42; n_mh=vYrW8M90nu-LD-hIJEMs1QvY2Pc6XEVeY9oEF5zUgOs; sso_uid_tt=04332b5b4937523e2c8e97029f7e19f4; sso_uid_tt_ss=04332b5b4937523e2c8e97029f7e19f4; toutiao_sso_user=2efed3be8fa6b75c715909bb71107e05; toutiao_sso_user_ss=2efed3be8fa6b75c715909bb71107e05; odin_tt=26ad6dedcf4df42be5626ebf207e4127cd7cb289e030fb56deed02bc5d901e93619e61681be7075dab4d2f196e8b4927a1a9978fd403459e094fb12ccc338dd9; passport_auth_status_ss=59e448ef2b8657ba73871420feeec18f%2C; sid_guard=2522f3210fc6a6a1b4bf951ef5c33a87%7C1629168451%7C5183999%7CSat%2C+16-Oct-2021+02%3A47%3A30+GMT; uid_tt=39aa60150b029633e32dec0fe5fbf267; uid_tt_ss=39aa60150b029633e32dec0fe5fbf267; sid_tt=2522f3210fc6a6a1b4bf951ef5c33a87; sessionid=2522f3210fc6a6a1b4bf951ef5c33a87; sessionid_ss=2522f3210fc6a6a1b4bf951ef5c33a87; sid_ucp_v1=1.0.0-KDg4MDIyYTc4ZDdjZWM1MTVlMWRmODQxNmI2ZjNiNDQ5ZDkzMzI3YTIKFQjquMXv-wIQw8bsiAYY7zE4BkD0BxoCbGYiIDI1MjJmMzIxMGZjNmE2YTFiNGJmOTUxZWY1YzMzYTg3; ssid_ucp_v1=1.0.0-KDg4MDIyYTc4ZDdjZWM1MTVlMWRmODQxNmI2ZjNiNDQ5ZDkzMzI3YTIKFQjquMXv-wIQw8bsiAYY7zE4BkD0BxoCbGYiIDI1MjJmMzIxMGZjNmE2YTFiNGJmOTUxZWY1YzMzYTg3; passport_auth_status=59e448ef2b8657ba73871420feeec18f%2C; MONITOR_WEB_ID=b4f69576-e1cd-44a0-8e0b-356434bb5a4b; douyin.com; csrf_session_id=cbb8c475a8404b4697e10a554fa35a46; s_v_web_id=verify_ksnywcsc_0Hu4CcfL_e4g5_4rrz_BnPZ_dwNssC3a49kB


GOOOD
ttwid=1%7Ch8p4qF9nCoBHx_pOoo7sWTjojl14ododBAAwR7wSolk%7C1629684858%7Cfea89d7edb3e634af61bbdeba87f88b0e2e32a459b28e9e671e88622cbf3d9c0; douyin.com; MONITOR_WEB_ID=0aa031d6-1bce-4baa-a89b-325ce6e762f0; s_v_web_id=verify_kso0adpa_jCZfwibg_rqeJ_4Ajk_B4tf_jsn8kj76y5hq; passport_csrf_token_default=9b2f2eac0a9f39ec37c468b36a7f6842; passport_csrf_token=9b2f2eac0a9f39ec37c468b36a7f6842; n_mh=kQ9gCOAKhni5cJE8BzIF7GmgrqMs-Ezyl6JopiWaKZQ; sso_uid_tt=fbd645b14201f2f19c359869da711884; sso_uid_tt_ss=fbd645b14201f2f19c359869da711884; toutiao_sso_user=8b35db1bc9ecb3e81305fa22af733090; toutiao_sso_user_ss=8b35db1bc9ecb3e81305fa22af733090; odin_tt=82a304b27219a90deae81d657af01197f09ca76defc9124f09758c3168b853a0b973679d0735e24cf67385d184c87acbf4f3796f31dc58aea7a6fbce7e414253; passport_auth_status_ss=57d8bfa1e5a81da0b5fdf9fcdaa68951%2C; sid_guard=083b6de46458b20f6f2c036ed2be2ab0%7C1629684874%7C5183999%7CFri%2C+22-Oct-2021+02%3A14%3A33+GMT; uid_tt=011120ed51164c6f0abb4fb8bbd411cc; uid_tt_ss=011120ed51164c6f0abb4fb8bbd411cc; sid_tt=083b6de46458b20f6f2c036ed2be2ab0; sessionid=083b6de46458b20f6f2c036ed2be2ab0; sessionid_ss=083b6de46458b20f6f2c036ed2be2ab0; sid_ucp_v1=1.0.0-KGVjNmUyZDMwZmRhYjJkYmM1MTZlNjJlNmNhOGYzYTNkMmRmYjZhYzAKFwjNyuDVhozSBhCKiYyJBhjvMTgGQPQHGgJsZiIgMDgzYjZkZTQ2NDU4YjIwZjZmMmMwMzZlZDJiZTJhYjA; ssid_ucp_v1=1.0.0-KGVjNmUyZDMwZmRhYjJkYmM1MTZlNjJlNmNhOGYzYTNkMmRmYjZhYzAKFwjNyuDVhozSBhCKiYyJBhjvMTgGQPQHGgJsZiIgMDgzYjZkZTQ2NDU4YjIwZjZmMmMwMzZlZDJiZTJhYjA; passport_auth_status=57d8bfa1e5a81da0b5fdf9fcdaa68951%2C
'''