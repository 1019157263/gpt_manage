# -*- coding:utf-8 -*-
"""
@desc: 
"""
import execjs
with open("../../statics/crawler_reverse.js", "r", encoding="utf-8") as f:
    crawler_js = f.read()
ctx = execjs.compile(crawler_js)
url = 'https://live.douyin.com/webcast/im/fetch/?aid=6383&live_id=1&device_platform=web&language=zh-CN&room_id=6994344394224601886&resp_content_type=protobuf&version_code=9999&identity=audience&internal_ext=fetch_time:1628499517613%7Cstart_time:0%7Cfetch_id:6994352162771857056%7Cflag:0%7Cseq:11%7Cnext_cursor:1628499517613_6994352167066824369_1_6994352132707057664%7Cdoor:3-n45&cursor=1628499517613_6994352167066824369_1_6994352132707057664&last_rtt=191&did_rule=3'
signature = ctx.call('sign', url)
print(signature)