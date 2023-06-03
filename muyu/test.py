import requests

class muyu:
    def __init__(self) :
        self.session = requests.session()
        self.singe_token = "b153c6e814f4601759b28206bfa6e469"
        hea= {
            "token":"8ea905dd-b03d-40e6-aac0-ce4350b762d0"
        }
        self.session.headers.update(hea)

    def adddyhao(self,zhuye):

        url = "http://muyu.doudouqwe.com/api/app/user_dyc/add"
        data = {
            "dy_url": zhuye,
            "file_url": "协议"
        }
        rawdata = self.session.post(url=url,data=data)
        print(rawdata.text)

if (__name__ == "__main__") :
    A = muyu()
    A.adddyhao("https://v.douyin.com/dRNN4sw/")