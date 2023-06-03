import requests,time,json
from requests.api import head, post

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
    def __init__(self) :
        self.li_not_ok = []
        self.session = requests.session()
        self.singe_token = "b153c6e814f4601759b28206bfa6e469"
        hea= {
            "token":"8ea905dd-b03d-40e6-aac0-ce4350b762d0"
        }
        self.session.headers.update(hea)

    def getone_task(self,type_s):
        #获取任务
        url = "http://muyu.doudouqwe.com/api/app/dy_taskc/getone"
        data = {
            "types": type_s,#2点赞.1关注
            "xpwiok_uid": "101970959466"#抖音id，领取任务 dy的Uid 如果不传用自己绑定的号做 绑定号详见 投手D音接口
        }
        onetask = self.session.post(url=url,data=data).json()   
        return onetask
        print(onetask)
    def puttask(self,dy_task_log_id,file_url):
        #提交任务
        url = f"http://muyu.doudouqwe.com/api/app/dy_task_logc/submit?dy_task_log_id={dy_task_log_id}&file_url={file_url}"
        raw_req = self.session.get(url)
        return raw_req



if __name__ ==  "__main__" :
    import os 
    A =muyuAPI()
    type_s = 1
    task = A.getone_task(type_s)
    cookies = "ttwid=1%7CwcxSnwdHna8fR0e9zJkTYtq0RlmPh0EQWGvOLbiFWcU%7C1629621048%7Ca2f3727bbe7c43503cece30916ff7836d6c0548c8a8152a741d318db6c09191e; douyin.com; MONITOR_WEB_ID=09db6820-28b3-4c78-9679-28412ad82697; passport_csrf_token_default=ab9f7a91b5fe776c8acbb38988f63ef1; passport_csrf_token=ab9f7a91b5fe776c8acbb38988f63ef1; s_v_web_id=verify_ksmyardk_mjJtZbuo_PECr_4l8J_9F8J_wf7n4f21E6vO; csrf_session_id=ec7aa248e3254e69b69edbba11aea3e4; n_mh=kQ9gCOAKhni5cJE8BzIF7GmgrqMs-Ezyl6JopiWaKZQ; sso_uid_tt=86351a5f0165d6d5af9ca54d8faefb77; sso_uid_tt_ss=86351a5f0165d6d5af9ca54d8faefb77; toutiao_sso_user=862d610a17c17a5655878d6ffdb956c9; toutiao_sso_user_ss=862d610a17c17a5655878d6ffdb956c9; odin_tt=bb68b7e37f81f3a06cef8e5ff9daca3d70723f4c16de33d2413979246d385854f325723f4db87e09474b14ed05318bf1dd1bbd2f7a3bb8b89ee5d5448ce9c609; passport_auth_status_ss=57a8a43bf36769a049439ce6064a1908%2C461df5550fd132fa2862fae71211d559; sid_guard=728655d7bd82affad2c213efdcea3a03%7C1629625944%7C5183999%7CThu%2C+21-Oct-2021+09%3A52%3A23+GMT; uid_tt=3bc458e2273caed1691844465f8fedd2; uid_tt_ss=3bc458e2273caed1691844465f8fedd2; sid_tt=728655d7bd82affad2c213efdcea3a03; sessionid=728655d7bd82affad2c213efdcea3a03; sessionid_ss=728655d7bd82affad2c213efdcea3a03; sid_ucp_v1=1.0.0-KDFkNDNmYzg2MTkwY2Q0ZTI4ODNlMjEzMWFkYzdmNjgyYzhlMTMzOGQKFwjNyuDVhozSBhDYvIiJBhjvMTgGQPQHGgJsZiIgNzI4NjU1ZDdiZDgyYWZmYWQyYzIxM2VmZGNlYTNhMDM; ssid_ucp_v1=1.0.0-KDFkNDNmYzg2MTkwY2Q0ZTI4ODNlMjEzMWFkYzdmNjgyYzhlMTMzOGQKFwjNyuDVhozSBhDYvIiJBhjvMTgGQPQHGgJsZiIgNzI4NjU1ZDdiZDgyYWZmYWQyYzIxM2VmZGNlYTNhMDM; passport_auth_status=57a8a43bf36769a049439ce6064a1908%2C461df5550fd132fa2862fae71211d559"
    token = "b153c6e814f4601759b28206bfa6e469"
    f = os.popen(f"python digg_follow_no_tk.py {cookies} {token} {type_s} {id}")
    print(f.read())
    print(task)


