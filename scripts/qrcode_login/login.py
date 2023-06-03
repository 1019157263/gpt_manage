# -*- coding:utf-8 -*-
"""
@desc: 
"""
import time
from io import BytesIO
import requests
import base64
from PIL import Image



class QRCodeLogin:
    headers = {
        'authority': 'www.douyin.com',
        'accept': 'application/json,text/javascript',
        'accept-language':'zh-CN,zh;q=0.9',
        'content-type':'application/x-www-form-urlencoded',
        'origin':'https://www.douyin.com',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.douyin.com/user/MS4wLjABAAAAgq8cb7cn9ByhZbmx-XQDdRTvFzmJeBBXOUO4QflP96M?enter_method=video_title&author_id=66598046050&group_id=6976510986547105060&log_pb=%7B%22impr_id%22%3A%22021624413357501fdbddc0100fff0020a9b342d0000001b0ac6ec%22%7D&enter_from=video_detail',
    }
    get_qrcode_url = 'https://sso.douyin.com/get_qrcode/?service=https%3A%2F%2Fwww.douyin.com%2F&need_logo=false&aid=6383'
    wait_scan_qrcode_url = 'https://sso.douyin.com/check_qrconnect/?service=https%3A%2F%2Fwww.douyin.com%2F&token={}&need_logo=false&aid=6383'

    def __init__(self):
        self.session = requests.session()
        self.session.headers = self.headers
        # self.session.proxies = {
        #     "https":"http://127.0.0.1:8888",
        #     "http":"http://127.0.0.1:8888"
        # }
        self.session.verify = False

    def login(self):
        # 获取二维码
        self.session.get("https://www.douyin.com")
        qrcode_response = self.session.get(self.get_qrcode_url)
        qrcode_content = qrcode_response.json()['data']['qrcode']
        image = Image.open(BytesIO(base64.b64decode(qrcode_content.encode())))
        image.show()
        token = qrcode_response.json()['data']['token']
        print(token)
        wait_scan_qrcode_url = self.wait_scan_qrcode_url.format(token)
        passport_csrf_token = self.session.cookies.get('passport_csrf_token')
        # self.session.headers.update({'x-tt-passport-csrf-token':passport_csrf_token})
        self.headers['x-tt-passport-csrf-token'] = passport_csrf_token
        while True:
            wait_scan_response = self.session.get(wait_scan_qrcode_url, headers=self.headers)
            print(wait_scan_response.json())
            status = wait_scan_response.json()['data']['status']
            time.sleep(1)
            if status == "3":
                break
        # 已经扫码
        redirect_url = wait_scan_response.json()['data']['redirect_url']
        response = self.session.get("https://sso.douyin.com/check_login/?service=https:%2F%2Fwww.douyin.com%2F&aid=6383").json()
        if response.get("has_login"):
            response = self.session.get(redirect_url)
            print(response.status_code)

        text = self.session.get('https://www.douyin.com').text
        print(self.session.cookies.get_dict())



if __name__ == '__main__':
    login = QRCodeLogin()
    login.login()