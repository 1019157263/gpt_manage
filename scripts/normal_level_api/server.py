# -*- coding:utf-8 -*-
"""
@desc: 
"""
import pprint
from urllib.parse import urlencode, quote

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'referer': 'https://www.douyin.com/video/6981060082599529764?previous_page=others_homepage',
}
session = requests.session()
session.headers = headers
session.verify = False
session.proxies = {
    # "https":"http://127.0.0.1:8888"
}

token = '35829f8c5447a2792ac4cc59dc50124e'


def do_request(url, login=False):
    data = {
        "url": url
    }
    resp = requests.post('http://59.110.158.68:8787/sign', data=data, headers={
        "Authorization":token
    }).json()
    print(resp)
    if resp['error_code'] == 0:
        _signature = resp['result']['_signature']
        url += "&" + urlencode({"_signature": _signature})
        response = session.get(url)
        print(url)
        return response


def user_search(keyword):
    keyword = quote(keyword)
    url = f'https://www.douyin.com/aweme/v1/web/discover/search/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_user_web&keyword={keyword}&search_source=normal_search&query_correct_type=1&is_filter_search=0&offset=0&count=18&version_code=160100&version_name=16.1.0'
    response = do_request(url)
    if response:
        users = ['%s %s' % (i['user_info']['uid'], i['user_info']['nickname']) for i in response.json()['user_list']]
        print('\n'.join(users))


def item_search(keyword):
    keyword = quote(keyword)
    url = f'https://www.douyin.com/aweme/v1/web/search/item/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_video_web&sort_type=0&publish_time=0&keyword={keyword}&search_source=normal_search&query_correct_type=1&is_filter_search=0&offset=0&count=30&version_code=160100&version_name=16.1.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F91.0.4472.101+Safari%2F537.36&browser_online=true'
    url = 'https://www.douyin.com/aweme/v1/web/search/item/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_video_web&sort_type=0&publish_time=0&keyword=%E7%BE%8E%E5%A5%B3&search_source=normal_search&query_correct_type=1&is_filter_search=0&offset=0&count=30&version_code=160100&version_name=16.1.0'
    response = do_request(url)
    if response:
        users = ['%s %s' % (i['aweme_info']['aweme_id'], i['aweme_info']['desc']) for i in response.json()['data']]
        print('\n'.join(users))


def user_info():
    session.get('https://www.douyin.com')
    url = 'https://www.douyin.com/aweme/v1/web/user/profile/other/?device_platform=webapp&aid=6383&channel=channel_pc_web&publish_video_strategy_type=2&source=channel_pc_web&sec_user_id=MS4wLjABAAAAAEtO1dCIZvj4VWbLU4Xce7DgVgsKNMNu88eNR2c2LtY&version_code=160100&version_name=16.1.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F90.0.4430.93+Safari%2F537.36&browser_online=true'
    response = do_request(url)
    if response:
        print(response.json()['user'])


def user_post():
    url = 'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAgq8cb7cn9ByhZbmx-XQDdRTvFzmJeBBXOUO4QflP96M&max_cursor=1625099137000&count=10&publish_video_strategy_type=2&version_code=160100&version_name=16.1.0'

    response = do_request(url)
    if response:
        users = ['%s %s' % (i['aweme_id'], i['desc']) for i in response.json()['aweme_list']]
        print('\n'.join(users))


def user_favorite():
    session.get('https://www.douyin.com')

    url = 'https://www.douyin.com/aweme/v1/web/aweme/favorite/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAgq8cb7cn9ByhZbmx-XQDdRTvFzmJeBBXOUO4QflP96M&max_cursor=0&min_cursor=0&count=10&publish_video_strategy_type=2&version_code=160100&version_name=16.1.0'
    response = do_request(url)
    if response:
        users = ['%s %s' % (i['aweme_id'], i['desc']) for i in response.json()['aweme_list']]
        print('\n'.join(users))


def item_comment(aweme_id=6927267289439980807):
    url = f'https://www.douyin.com/aweme/v1/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id={aweme_id}&cursor=0&count=30&version_code=160100&version_name=16.1.0'

    session.get('https://www.douyin.com')
    response = do_request(url)
    if response:
        users = ['%s %s' % (i['user']['nickname'], i['text']) for i in response.json()['comments']]
        print('\n'.join(users))


if __name__ == '__main__':
    # user_search('陈赫')
    item_search('美女')
    # item_comment()
    # user_favorite()
    # user_post()
    # user_info()
