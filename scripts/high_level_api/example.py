# -*- coding:utf-8 -*-
"""
@desc: 
"""
import requests

cookie = 'your cookie'
token = '30d8fd4fc3fefdad04b75bab909611cf'
class DouyinHighLevelAPI:
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
        'referer': 'https://www.douyin.com/user/MS4wLjABAAAAgq8cb7cn9ByhZbmx-XQDdRTvFzmJeBBXOUO4QflP96M?enter_method=video_title&author_id=66598046050&group_id=6976510986547105060&log_pb=%7B%22impr_id%22%3A%22021624413357501fdbddc0100fff0020a9b342d0000001b0ac6ec%22%7D&enter_from=video_detail',
        'accept': '*/*',
        "x-secsdk-csrf-request": "1",
        "x-secsdk-csrf-version": "1.2.7",
    }
    api = 'http://59.110.158.68:8787/sign_v3'

    def __init__(self, cookie):
        cookies = {i.split("=", maxsplit=1)[0]: i.split("=", maxsplit=1)[1] for i in cookie.split("; ") if
                   len(i.split("=", maxsplit=1)) >= 2}
        session = requests.session()
        session.headers = self.headers
        session.cookies.update(cookies)
        cookies.pop('csrf_session_id', None)
        # 获取x-secsdk-csrf-token
        # response = session.head('https://www.douyin.com/aweme/v1/web/commit/follow/user/', headers=self.headers)
        response = session.head('https://www.douyin.com/aweme/v1/web/commit/item/digg/', headers=self.headers)
        token = response.headers.get('X-Ware-Csrf-Token')
        if not token:
            raise ValueError("获取token失败,请确认cookie有效")
        self.headers['x-secsdk-csrf-token'] = token.split(",")[1]
        self.headers.pop('x-secsdk-csrf-request')
        self.headers.pop('x-secsdk-csrf-version')
        self.session = session

    def digg(self, aweme_id="6984008368784477454"):
        digg_url = 'https://www.douyin.com/aweme/v1/web/commit/item/digg/?device_platform=webapp&aid=6383&channel=channel_pc_web&version_code=160100&version_name=16.1.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F91.0.4472.101+Safari%2F537.36&browser_online=true'

        data = {
            "url": digg_url,
            "body": "type=1&aweme_id=%s" % aweme_id
        }
        response = requests.post(self.api, data=data, headers={
            "Authorization":token
        }).json()
        print(response)
        if response['error_code'] == 0:
            sign = response['result']['_signature']
            if sign:
                digg_url += "&_signature=" + sign
                response = self.session.post(digg_url, headers=self.headers, data={
                    "aweme_id": aweme_id,
                    "type": "1"
                })
                print(response)
                try:
                    print(response.json())
                except:
                    print(response.text)

    def follow(self, user_id="66598046050"):
        follow_url = "https://www.douyin.com/aweme/v1/web/commit/follow/user/?device_platform=webapp&aid=6383&channel=channel_pc_web&version_code=160100&version_name=16.1.0"

        data = {
            "url": follow_url,
            "body": "type=1&user_id=%s" % user_id
        }
        response = requests.post(self.api, data=data, headers={
            "Authorization":token
        }).json()
        print(response)
        if response['error_code'] == 0:
            sign = response['result']['_signature']
            if sign:
                follow_url += "&_signature=" + sign
                data = {
                    "type": "1",
                    "user_id": user_id
                }
                response = self.session.post(follow_url, headers=self.headers, data=data)
                print(response)
                try:
                    print(response.json())
                except:
                    print(response.text)


if __name__ == '__main__':
    douyin = DouyinHighLevelAPI(cookie)
    # douyin.follow()
    douyin.digg()
