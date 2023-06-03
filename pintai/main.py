import requests
class job:
    def __init__(self) :
        self.S = requests.session()
        self.user = {
            "username":"1019157263",
            "password":"a1019157263"

        }
    def login(self):
        url= "http://www.o7c.com/api.php/home/index/user_login"
        A = self.S.post(url=url,data=self.user)
        print(A.text)
    
    def bind_user(self):
        url="http://www.o7c.com/api.php/home/index/user_bind_tiktok_main"
        #101970959466
        data = {
            "username" : self.user["username"],
            "password" : self.user["password"],
            "tiktok_num":f"https://www.iesdouyin.com/share/user/{self.uid}?sec_uid={self.sec_uid}"

        }
    def get_task(self,):
        url = "http://www.o7c.com/api.php/home/follow/get_task"
        data = {
            "tiktok_num":"dy_name",
        }


if __name__ == "__main__" :
    A = job()
    A.login()
