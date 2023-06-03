# -*- coding:utf-8 -*-
"""
@desc: 
"""
from urllib.parse import urlencode, quote

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'referer': 'https://www.douyin.com/video/6981060082599529764?previous_page=others_homepage',
}
session = requests.session()
session.headers = headers

def do_request(url, login=False):
    data = {
        "method": "GET",
        "url": url
    }
    resp = requests.post('http://127.0.0.1:5000/sign', data=data, headers={
        "Authorization":"1adb422345309d6d42408ad45b1f5fb3"
    }).json()
    print(resp)
    if resp['error_code'] == 0:
        _signature = resp['result']['_signature']
        url += "&" + urlencode({"_signature": _signature})
        response = session.get(url)
        print(response)
        print(response.url)
        print(response.json())

def user_search(keyword):
    keyword = quote(keyword)
    url = f'https://www.douyin.com/aweme/v1/web/discover/search/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_user_web&keyword={keyword}&search_source=normal_search&query_correct_type=1&is_filter_search=0&offset=0&count=18&version_code=160100&version_name=16.1.0'
    do_request(url)

def item_search(keyword):
    keyword = quote(keyword)
    url = f'https://www.douyin.com/aweme/v1/web/search/item/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_video_web&sort_type=0&publish_time=0&keyword={keyword}&search_source=normal_search&query_correct_type=1&is_filter_search=0&offset=0&count=24&version_code=160100&version_name=16.1.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F91.0.4472.101+Safari%2F537.36&browser_online=true'

    do_request(url)

def user_info():
    session.get('https://www.douyin.com')
    url = 'https://www.douyin.com/aweme/v1/web/user/profile/other/?device_platform=webapp&aid=6383&channel=channel_pc_web&publish_video_strategy_type=2&source=channel_pc_web&sec_user_id=MS4wLjABAAAAAEtO1dCIZvj4VWbLU4Xce7DgVgsKNMNu88eNR2c2LtY&version_code=160100&version_name=16.1.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F90.0.4430.93+Safari%2F537.36&browser_online=true'
    do_request(url)

def user_post():
    url = 'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAgq8cb7cn9ByhZbmx-XQDdRTvFzmJeBBXOUO4QflP96M&max_cursor=1625099137000&count=10&publish_video_strategy_type=2&version_code=160100&version_name=16.1.0'

    do_request(url)

def user_favorite():
    session.get('https://www.douyin.com')

    url = 'https://www.douyin.com/aweme/v1/web/aweme/favorite/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAgq8cb7cn9ByhZbmx-XQDdRTvFzmJeBBXOUO4QflP96M&max_cursor=0&min_cursor=0&count=10&publish_video_strategy_type=2&version_code=160100&version_name=16.1.0'
    do_request(url)

def item_comment():
    url = 'https://www.douyin.com/aweme/v1/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=6927267289439980807&cursor=20&count=20&version_code=160100&version_name=16.1.0'
    do_request(url)

def live():
    url = 'https://live.douyin.com/webcast/im/fetch/?aid=6383&live_id=1&device_platform=web&language=zh-CN&room_id=6989496653246761736&resp_content_type=protobuf&version_code=9999&identity=audience&internal_ext=&cursor=0&last_rtt=-1&did_rule=3'
    do_request(url)
if __name__ == '__main__':
    # user_search('陈赫')
    item_search('迈巴赫')
    # item_comment()
    # user_favorite()
    # user_info()
    # live()
