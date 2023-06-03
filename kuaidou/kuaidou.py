from re import S
import re
import requests 

from digg_follow_no_tk import DouyinHighLevelAPI

class kuaidou:
    def __init__(self) :
        self.S =  requests.session()
        head = {"Content-Type": "application/x-www-form-urlencoded"}
        self.S .headers.update(head)

    def login(self,name,pwd):
        data = {
            "username":name,
            "password" :pwd
             }
        url = "http://iapp.dxdxin.com/app/account/login"
        raw = self.S.post(url=url,data=data)
        # print (raw.json())
        return raw.json()
    def getone(self,token):
        url = "http://iapp.dxdxin.com/app/dyin/pull/one"
        hea = {
            "Token":token
        }
        data = {
            "access":0b1111111,
            "bSlow":False,
        }
        raw = self.S.post(url=url,data=data,headers=hea)
        print(raw.text)
        return raw.json()
    def submitone(self,job):
        url = "http://iapp.dxdxin.com/app/dyin/submit/one"
        hea = {
            "Token":token
        }
        data = {
            "id":job["data"]["id"],
            "shot_img":"协议",
        }
        raw = self.S.post(url=url,data=data,headers=hea)
        print(raw.text)

class kuaidou_x:
    def __init__(self) :
        self.S =  requests.Session()
        head = {"Content-Type": "application/x-www-form-urlencoded"}
        self.S .headers.update(head)
    def getone(self,uid):
        url = "http://sapp.dxdxin.com/app/simp/dyin/pull/one"
        data = {
            "username":"15603001320",
            "dyuserid":f"{uid}",
            "access":1
        }
        print(data)
        raw = self.S.post(url=url,data=data)
        return raw.json()
    
    def submitone(self,job):
        url = "http://sapp.dxdxin.com/app/simp/dyin/submit/one"
        data = {
            "username":"15603001320",
            "id":job["data"]["id"]
        }
        raw = self.S.post(url=url,data=data)
        print(raw.text)

    
if (__name__ == "__main__") :
    # A = kuaidou()
    # token = A.login("18381801393","a1019157263")["data"]["token"]
    # job  = A.getone(token)
    # A.submitone(job)
    singe_token = "b153c6e814f4601759b28206bfa6e469"
    douyinapi = DouyinHighLevelAPI("ttwid=1%7C-jFWDaAPUfeuvyHn-TOl2Tw2IFwdOJx6w5GpWEycHTI%7C1629790120%7Cea8e1af1ee5bac6ba7cadb42a7f17d0014284dc6f3e34d9e0a45d5432d776ea4; douyin.com; passport_csrf_token_default=e46c2c49a210aa71e54c1e5be7f76a55; passport_csrf_token=e46c2c49a210aa71e54c1e5be7f76a55; s_v_web_id=verify_kspqymjj_tP9Uon2o_YUFx_46iX_9mtq_wgA4rDQ2mJne; n_mh=9_eSs120dI5my_xv8AqoEy3n1_4F7UYEXxRroId6tVU; sso_uid_tt=4a21de94f44455df5bb89d61e1928682; sso_uid_tt_ss=4a21de94f44455df5bb89d61e1928682; toutiao_sso_user=bac0fa01cf45454b9aecc0214f6a4bce; toutiao_sso_user_ss=bac0fa01cf45454b9aecc0214f6a4bce; odin_tt=31d61d73332c36ee8382684acd52adda3536ac58993141598d7c1e637d2ab4874c0bddca9ca383e9b95955feebcdab8495451c9568a644dda52290ce59f75ec0; passport_auth_status_ss=23ae35313483eaa35995502aab01fb61%2C; sid_guard=4e69ed159fa58bca3b2b5ff7fc5f8b1c%7C1629790154%7C5183998%7CSat%2C+23-Oct-2021+07%3A29%3A12+GMT; uid_tt=c283fd2b6e5d204257e359066dba52d4; uid_tt_ss=c283fd2b6e5d204257e359066dba52d4; sid_tt=4e69ed159fa58bca3b2b5ff7fc5f8b1c; sessionid=4e69ed159fa58bca3b2b5ff7fc5f8b1c; sessionid_ss=4e69ed159fa58bca3b2b5ff7fc5f8b1c; sid_ucp_v1=1.0.0-KDNhYjdjNmY2MjVhN2ZlM2I4MzljMWQ1NGI4NGI3ZDllMjVmMzIzYTIKFwiI3vDNpIyaAhDKv5KJBhjvMTgGQPQHGgJsZiIgNGU2OWVkMTU5ZmE1OGJjYTNiMmI1ZmY3ZmM1ZjhiMWM; ssid_ucp_v1=1.0.0-KDNhYjdjNmY2MjVhN2ZlM2I4MzljMWQ1NGI4NGI3ZDllMjVmMzIzYTIKFwiI3vDNpIyaAhDKv5KJBhjvMTgGQPQHGgJsZiIgNGU2OWVkMTU5ZmE1OGJjYTNiMmI1ZmY3ZmM1ZjhiMWM; passport_auth_status=23ae35313483eaa35995502aab01fb61%2C; MONITOR_WEB_ID=d9c1f50b-d5f7-4d53-a628-18528a8b77a0",singe_token)
    uid = douyinapi.uid
    A = kuaidou_x()
    job = A.getone(uid)
    print(job)
    req_ret =douyinapi.digg(aweme_id=job["data"]["aweme_id"]).json()
    print(req_ret)
    A.submitone(job)

    