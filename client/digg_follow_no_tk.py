# -*- coding:utf-8 -*-
"""
@desc: 
"""
import time

import requests

# from scripts import cookie

# token = 'b153c6e814f4601759b28206bfa6e469'
class DouyinHighLevelAPI:
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
        'referer': 'https://www.douyin.com/user/MS4wLjABAAAAgq8cb7cn9ByhZbmx-XQDdRTvFzmJeBBXOUO4QflP96M?enter_method=video_title&author_id=66598046050&group_id=6976510986547105060&log_pb=%7B%22impr_id%22%3A%22021624413357501fdbddc0100fff0020a9b342d0000001b0ac6ec%22%7D&enter_from=video_detail',
        'accept': '*/*',
        "x-secsdk-csrf-request": "1",
        "x-secsdk-csrf-version": "1.2.7",
    }
    # api = 'http://59.110.158.68:8787/sign_v3'
    api = 'http://127.0.0.1:8000/token/'

    def __del__(self):
        print("接口对象关闭")
        try:
            self.session.close()
        except Exception as e:
            
            print(e)
            session = requests.session()

            
        # self.session.close()
    def __init__(self, cookie,token_token):
        self.token_token = token_token
        cookies = {i.split("=", maxsplit=1)[0]: i.split("=", maxsplit=1)[1] for i in cookie.split("; ") if
                   len(i.split("=", maxsplit=1)) >= 2}
        print(cookies)
        # session = requests.session()
        # session.close()
        session = requests.session()
        session.headers = self.headers
        session.cookies.update(cookies)
        cookies.pop('csrf_session_id', None)
        # 获取x-secsdk-csrf-token
        # response = session.head('https://www.douyin.com/aweme/v1/web/commit/follow/user/', headers=self.headers)
        response = session.head('https://www.douyin.com/aweme/v1/web/commit/item/digg/', headers=self.headers)
        token = response.headers.get('X-Ware-Csrf-Token')
        print(token)
        if not token:
            print(f"[cookies]{cookie}")
            raise ValueError("获取token失败,请确认cookie有效")
        self.headers['x-secsdk-csrf-token'] = token.split(",")[1]
        self.headers.pop('x-secsdk-csrf-request')
        self.headers.pop('x-secsdk-csrf-version')
        self.session = session

    def digg(self, aweme_id="6990193653150993664"):
        #点赞
        digg_url = 'https://www.douyin.com/aweme/v1/web/commit/item/digg/?device_platform=webapp&aid=6383&channel=channel_pc_web&version_code=160100&version_name=16.1.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F91.0.4472.101+Safari%2F537.36&browser_online=true'

        data = {
            "url": digg_url,
            "body": "type=1&aweme_id=%s" % aweme_id
        }
        response = requests.post(self.api, data=data, headers={
            "Authorization":self.token_token
        })
        response = response.json()
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


    def follow(self, user_id="3853137110125559"):
        #关注
        # 105994442903
        # 3853137110125559
        # "https://www.douyin.com/aweme/v1/web/user/profile/self/?device_platform=webapp&aid=6383&channel=channel_pc_web&publish_video_strategy_type=2&source=channel_pc_web&version_code=160100&version_name=16.1.0&cookie_enabled=true&screen_width=1368&screen_height=912&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F92.0.4515.159+Safari%2F537.36&browser_online=true&_signature=_02B4Z6wo00d01KOzvIAAAIDAI7FGworj5pCjs7gAAEn3b8"
        follow_url = "https://www.douyin.com/aweme/v1/web/commit/follow/user/?device_platform=webapp&aid=6383&channel=channel_pc_web&version_code=160100&version_name=16.1.0"
        follow_url = "https://www.douyin.com/aweme/v1/web/commit/follow/user/?device_platform=webapp&aid=6383&channel=channel_pc_web&version_code=160100&version_name=16.1.0&cookie_enabled=true&screen_width=1368&screen_height=912&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F92.0.4515.159+Safari%2F537.36&browser_online=true"
        
        typez=1
        data = {
            "url": follow_url,
            "body": f"type={typez}&user_id=%s" % user_id
        }
        response = requests.post(self.api, data=data, headers={
            "Authorization":self.token_token
        }).json()
        print(response)
        if response['error_code'] == 0:
            sign = response['result']['_signature']
            if sign:
                follow_url += "&_signature=" + sign
                data = {
                    "type": f"{typez}",
                    "user_id": user_id
                }
                response = self.session.post(follow_url, headers=self.headers, data=data)
                print(response)
                try:
                    print(response.json())
                except:
                    print(response.text)

                    
if __name__ == '__main__':
    
    douyin = DouyinHighLevelAPI("ttwid=1%7CJwEWlAiaGoGS6-81RbiP57snFHf10HNGPuxomIRo6NM%7C1625226422%7C60a687cdd94c533a28fd0f30ae4d4024bfcc918feb0f63922254fc6597969d96; sessionid_ss=cf37bc2390a2469dc1ae2c1e2586519e","b153c6e814f4601759b28206bfa6e469")
    douyin.digg()

    # # # douyin = DouyinHighLevelAPI("ttwid=1%7CGryCFE1N45WnOqqUwEmiC7xOpkPiCBNBAtVf4sorLqk%7C1629378995%7C8470b7d4bb816a6c0ef69ac779749108c1aec9f1343c2f63876a56602da3663a; douyin.com; passport_csrf_token_default=a29362dd53580eefab881d99d75da818; passport_csrf_token=a29362dd53580eefab881d99d75da818; s_v_web_id=verify_ksiy6ryj_ZDqhFEOy_agUn_4RJr_BQJw_hUHWriliknAL; n_mh=9-mIeuD4wZnlYrrOvfzG3MuT6aQmCUtmr8FxV8Kl8xY; sso_uid_tt=4ffa4d80f274ac4406c6b028c325a133; sso_uid_tt_ss=4ffa4d80f274ac4406c6b028c325a133; toutiao_sso_user=4fcb6f60421f5803f61571e57bbb3b8f; toutiao_sso_user_ss=4fcb6f60421f5803f61571e57bbb3b8f; odin_tt=416a0365cdfce16ee0f5fedb3be36f5ce2b450d3aa47347c085cbdc555efd7eaf2c8e7112299a1bedc10ec7966c1bbb89aebfa360ba82ff55048bb770c3117a7; passport_auth_status_ss=21ea276df0826cf2d69c96e3546f17d8%2C; sid_guard=6f3b58ce93d0ecfe7d0b587d252f8b12%7C1629379365%7C5183999%7CMon%2C+18-Oct-2021+13%3A22%3A44+GMT; uid_tt=0f85f8ce96dfe423b3e2b19af825007f; uid_tt_ss=0f85f8ce96dfe423b3e2b19af825007f; sid_tt=6f3b58ce93d0ecfe7d0b587d252f8b12; sessionid=6f3b58ce93d0ecfe7d0b587d252f8b12; sessionid_ss=6f3b58ce93d0ecfe7d0b587d252f8b12; sid_ucp_v1=1.0.0-KDM5NmVhNWEzYTY5YWM5YmIyNjc3ZmJjMjIyMjc0NGI2ODk4MjE3MGEKFwjH_uD16Y3AARCltvmIBhjvMTgGQPQHGgJsZiIgNmYzYjU4Y2U5M2QwZWNmZTdkMGI1ODdkMjUyZjhiMTI; ssid_ucp_v1=1.0.0-KDM5NmVhNWEzYTY5YWM5YmIyNjc3ZmJjMjIyMjc0NGI2ODk4MjE3MGEKFwjH_uD16Y3AARCltvmIBhjvMTgGQPQHGgJsZiIgNmYzYjU4Y2U5M2QwZWNmZTdkMGI1ODdkMjUyZjhiMTI; passport_auth_status=21ea276df0826cf2d69c96e3546f17d8%2C; MONITOR_WEB_ID=d55f9a0a-12f8-4089-8089-87dc23de94c2")
    
#     # # douyin.digg()
    # # while True:
    # #     douyin.digg()
    # #     # douyin.follow()

    # #     time.sleep(1)