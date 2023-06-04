from math import radians
from django.shortcuts import render
import json,time
# Create your views here.
from django.http import HttpResponse
# import execjs
import sys
import django.utils.timezone as timezone
import datetime
from .models import tokens,loging,user_cookies,user_admin,liaotian
import binascii
# from pyDes import des, CBC, PAD_PKCS5
import base64
from django.http import StreamingHttpResponse

# def des_encrypt(s):
#     """
#     DES 加密
#     :param s: 原始字符串
#     :return: 加密后字符串，16进制
#     """
#     secret_key = '20171117'
#     iv = secret_key
#     k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
#     en = k.encrypt(s, padmode=PAD_PKCS5)
#     # print("8899999888888888888888888888888888")
#     # print(type(en))
#     # b = base64.b64encode(en)
#     # print(b)


#     return binascii.b2a_hex(en)

# def des_descrypt(s):
#     """
#     DES 解密
#     :param s: 加密后的字符串，16进制
#     :return: 解密后的字符串
#     """
#     secret_key = '20171117'
#     iv = secret_key
#     k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
#     de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
#     return de














print ("*************************")
print(time.time())
print (sys.argv[0])

driver = None
with open("./statics/crawler_reverse.js", "r", encoding="utf-8") as f:
    crawler_js = f.read()
# ctx = execjs.compile(crawler_js)








user_ag_list = [
            #华为
            "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 8.1; PAR-AL00 Build/HUAWEIPAR-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/WIFI Language/zh_CN Process/tools",
            "Mozilla/5.0 (Linux; Android 8.1.0; ALP-AL00 Build/HUAWEIALP-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.1.0)",
            "Mozilla/5.0 (Linux; Android 8.1; EML-AL00 Build/HUAWEIEML-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.143 Crosswalk/24.53.595.0 XWEB/358 MMWEBSDK/23 Mobile Safari/537.36 MicroMessenger/6.7.2.1340(0x2607023A) NetType/4G Language/zh_CN",
            "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 8.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/NON_NETWORK Language/zh_CN Process/tools",
            "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.4.950 UWS/2.11.1.50 Mobile Safari/537.36 AliApp(DingTalk/4.5.8) com.alibaba.android.rimet/10380049 Channel/227200 language/zh-CN",
            "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; EML-AL00 Build/HUAWEIEML-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.4.974 UWS/2.13.1.48 Mobile Safari/537.36 AliApp(DingTalk/4.5.11) com.alibaba.android.rimet/10487439 Channel/227200 language/zh-CN",
            "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; EML-TL00 Build/HUAWEIEML-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.4.974 UWS/2.14.0.13 Mobile Safari/537.36 AliApp(TB/7.10.4) UCBS/2.11.1.1 TTID/227200@taobao_android_7.10.4 WindVane/8.3.0 1080X2244",
            "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; HUAWEI MT1-U06 Build/HuaweiMT1-U06) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/042_2.7.3_diordna_8021_027/IEWAUH_61_2.1.4_60U-1TM+IEWAUH/7300001a/91E050E40679F078E51FD06CD5BF0A43%7C544176010472968/1",
            "Mozilla/5.0 (Linux; Android 8.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/4G Language/zh_CN Process/tools",
            "Mozilla/5.0 (Linux; U; Android 10; zh-cn; COL-AL10 Build/HUAWEICOL-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/12.0 Mobile Safari/537.36 COVC/045817",


            #"苹果：",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/6.7.3(0x16070321) NetType/WIFI Language/zh_CN",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/6.7.3(0x16070321) NetType/WIFI Language/zh_HK",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.8.2 Mobile/15B87 Safari/604.1 MttCustomUA/2 QBWebViewType/1 WKType/1",
            "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.3.0 Mobile/15B87 Safari/604.1 MttCustomUA/2 QBWebViewType/1 WKType/1",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.8.2 Mobile/14B72c Safari/602.1 MttCustomUA/2 QBWebViewType/1 WKType/1",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_2 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A421 wxwork/2.5.8 MicroMessenger/6.3.22 Language/zh",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 wxwork/2.5.1 MicroMessenger/6.3.22 Language/zh",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.8.2 Mobile/14B100 Safari/602.1 MttCustomUA/2 QBWebViewType/1 WKType/1",
            #"维沃和欧珀：",
            "Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baidubrowser/7.18.21.0 (Baidu; P1 6.0.1)",
            "Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.10 (Baidu; P1 6.0.1)",
            "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; vivo Y85 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.6.976 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 5.1.1; OPPO R9 Plustm A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.12 baiduboxapp/10.12.0.12 (Baidu; P1 5.1.1)",
            "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 7.1.1)",
            "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044207 Mobile Safari/537.36 MicroMessenger/6.7.3.1340(0x26070332) NetType/4G Language/zh_CN Process/tools",
            "Mozilla/5.0 (Linux; Android 8.1.0; PACM00 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.1.0)",
            "Mozilla/5.0 (Linux; Android 7.1.1; vivo X20A Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.2.1340(0x2607023A) NetType/WIFI Language/zh_CN",
            "Mozilla/5.0 (Linux; Android 7.1.1; vivo X20A Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.2.1340(0x2607023A) NetType/WIFI Language/zh_CN",
            "Mozilla/5.0 (Linux; Android 8.1.0; vivo Y71A Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.1.0)",
            #"小米：",
            "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; Mi Note 2 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.1",
            "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5s Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.2.2",
            "Mozilla/5.0 (Linux; Android 8.0.0; MI 6 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.0.0)",
            "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MI 5 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.9.969 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 8.0.0; MI 6 Build/OPR1.170623.027) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 Maxthon/3235",
            "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; Mi Note 3 Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.0.2",
            #"三星：",
            "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; SM-J3109 Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.0.960 UWS/2.12.1.18 Mobile Safari/537.36 AliApp(TB/7.5.4) UCBS/2.11.1.1 WindVane/8.3.0 720X1280",
            "Mozilla/5.0 (Linux; Android 8.0.0; SM-G9650 Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.0.0)",
            "Mozilla/5.0 (Linux; Android 8.0.0; SM-N9500 Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.0.0)"
]














import time,random
import datetime
 
# # 字符型日期转日期型（datetime）
# print(datetime.datetime.strptime("2022-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"))




 




class DateUtils:
 
    # 获取两个timezone的天数差
    @staticmethod
    def get_difference(start, end):
        start_time = start.strftime('%Y-%m-%d %H:%M:%S')
        end_time = end.strftime('%Y-%m-%d %H:%M:%S')
        now = time.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        old = time.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        delta_seconds = time.mktime(now) - time.mktime(old)
        return delta_seconds / 3600 / 24
 
    # 时间戳转换为时间timezone
    @staticmethod
    def get_date_by_timestamp(self, delta_seconds):
        try:
            time_array = time.localtime(int(delta_seconds))
            other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        except Exception as e:
            return e
        return other_style_time
 
    # 将timezone时间转换为时间戳
    def get_timestamp_by_date(self, date):
        origin_time = date.strftime('%Y-%m-%d %H:%M:%S')
        target_time = time.strptime(origin_time, '%Y-%m-%d %H:%M:%S')
        return time.mktime(target_time)
 
    # 根据一个时间-时间戳来计算另一个时间
    def get_date_by_date_time_stamp(self, date, timestamp):
        d1 = self.get_date_by_timestamp(timestamp)
        return self.get_difference(d1, date)



def istokenok(token):
    
    ret={
            "error_code": 1,#1失败
            "reason": "失败,token不存在,请联系购买。",
            "token":token,
            # "balance":balance,
            "result": {
                "_signature": "no token"
            }
                }
    
    t = time.time()#现在时间
    token_purchasetime = time.mktime(token.purchasetime.timetuple())+28800#不明原因慢了8小时，购买时间+8小时（28800秒）
    print(f"现在时间{t}，购买时间{token_purchasetime}")
    '''
    现在时间1629443380.8602288，购买时间1629396720.0
    '''
    token_timelength = token.timelength#token时长
    print(token_timelength)
    tiemlenth=t-token_purchasetime
    print(tiemlenth)
    

    ret["timelength"] = token_timelength-tiemlenth
    ret["balance"] = token.balance

    isok = False
    if(token.isBanned ):
        print("token被封禁")
        ret["error_code"]=1#1失败
        ret["reason"] = "token被封禁"+token.remark
    elif(tiemlenth>token_timelength):
        print("token已过期")
        ret["error_code"]=1#1失败
        ret["reason"] = "token已过期,请续费。"
    elif(token.balance <= 0):
        print("token点数不足")
        ret["error_code"]=1#1失败
        ret["reason"] = "token点数不足,请充值。"
    elif(token.isBanned ):
        print("token被封禁")
        ret["error_code"]=1#1失败
        ret["reason"] = token.remark
    else:
        print("成功")
        ret["error_code"]=0#成功
        ret["reason"] = "成功"
    return ret
# def job_t2e(raw,token):
    B =""
    n= 0
    # print(raw.type())

    ret = raw.replace("\\r","").replace("\n\n","").split("\n")
    # print(ret)
    # print(ret.type())
    ret_list = ret
    
    for i in ret_list :
        print(i)
        it = i.replace("\\r","").replace("\n","").strip()
        q = f"{it}----{random.sample(user_ag_list, 1)[0]}"
        # print("qqqqqqqqqqqqqqqqqqqqqqqqqqqq")
        print(q)
        try:
            miwen = des_encrypt(q)
            B=B+"Environment://"+str(miwen,"utf-8")+"\n"
            n += 1
            token.balance -=1
            token.save()
        except Exception as e:
            print ("job")
            print (e)
            continue
    
    now = datetime.datetime.now()
    print()
    tn = now.strftime("%Y-%m-%d %H:%M:%S")
    retx = f"{tn} 成功提取{n}/{len(ret_list)}个\n{B}"
    return retx       
    
     
def convert_time_to_str(time):
    #时间数字转化成字符串，不够10的前面补个0
    if (time < 10):
        time = '0' + str(time)
    else:
        time=str(time)
    return time

def sec_to_data(y):

    h=int(y//3600 % 24)
    d = int(y // 86400)
    m =int((y % 3600) // 60)
    s = round(y % 60,2)
    h=convert_time_to_str(h)
    m=convert_time_to_str(m)
    s=convert_time_to_str(s)
    d=convert_time_to_str(d)
    # 天 小时 分钟 秒
    return d + "天" + h + "时" + m + "分" + s+"秒"


def isok(request):
    if request.method == 'GET':
        
        context = {
            'token': '',
            'input': '',
            'output': '',

        }
        return render(request, 'tokenapps/t2e.html',context)
    if request.method == 'POST':
        try:
            token = request.POST.get('token')
            raw = request.POST.get('raw_token')
            print(token)
            print(raw)
            if(token == None or raw == None):
                return HttpResponse("出错了...")

            try:
                token_raw =  tokens.objects.get(token=token)
                ret_token = istokenok(token_raw)
                print(ret_token)
                if(ret_token["error_code"] == 0):#正常返回密文环境
                    print("--------------------------------------")

                    print(type(raw))
                    # out_put = job_t2e(raw,token_raw)#加密,扣点
                    # print(out_put)

                    print("--------------------------------------")
                    

                    # x = des_encrypt(raw.encode())
                    # xd = des_descrypt(x)
                    # print(xd)

                    timeStamp = ret_token["timelength"]

                    timeArray = time.localtime(timeStamp)

                    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

                    minfo=f'''
                    剩余时间:{sec_to_data(ret_token["timelength"])} ，剩余数量:{ret_token["balance"]}

                    '''
                    context = {
                        'token': token,
                        'input': raw,
                        "info":minfo,
                        'output': "out_put",
                    }
                    print("-----------------------------------")
                    print(context)
                    log = loging(users = token,mse = json.dumps(context),state="环境")
                    log.save()
                    return render(request, 'tokenapps/t2e.html',context)
                else:
                    return HttpResponse(json.dumps(token_raw),content_type='application/json')

            except Exception as e:
                print(e)
                return HttpResponse(json.dumps(token_raw),content_type='application/json')
        except:
                return HttpResponse("出错了...")
modle = "gpt-3.5-turbo-0301"

def ret_stem(id,token,ob):
    qa = ""
    yield json.dumps({"role":"assistant","id":id,"parentMessageId":id,"text":"","detail":{"id":id,"object":"chat.completion.chunk","created":time.time(),"model":modle,"choices":[{"delta":{"role":"assistant"},"index":0,"finish_reason":None}]}})
    yield "\r\n"
    for i in ob:
        try:
            # print(i)
            yret = i['choices'][0]['delta']["content"]   #extract the message
            qa+=yret
            x_ret = json.dumps({"role":"assistant","id":id,"parentMessageId":id,"text":qa,"delta":qa,"detail":{"id":id,"object":"chat.completion.chunk","created":time.time(),"model":"gpt-3.5-turbo-0301","choices":[{"delta":{"content":yret},"index":0,"finish_reason":None}]}})
            # print(x_ret)
            '''
            {"role":"assistant","id":id,"parentMessageId":id,"text":"","detail":{"id":id,"object":"chat.completion.chunk","created":time.time(),"model":"gpt-3.5-turbo-0301","choices":[{"delta":{"role":"assistant"},"index":0,"finish_reason":null}]}}
            
            '''
            print(x_ret)
            
            yield x_ret
            yield "\r\n"
            
            # # print(chunk_message,)
        except:
            # yield "*"
            pass
    oss  = {"role":"assistant","id":id,"parentMessageId":id,"text":qa,"detail":{"id":id,"object":"chat.completion.chunk","created":time.time(),"model":"gpt-3.5-turbo-0301","choices":[{"delta":{},"index":0,"finish_reason":"stop"}]}}
    log = loging(users = token,mse = json.dumps(oss, ensure_ascii=False, indent=4),state="AI回答")
    log.save()
    
    liaotian_info =  liaotian.objects.get(uid=id)#获取token对象
    liaotian_mes = json.loads(liaotian_info.mse)
    liaotian_mes.append({"role": "assistant","content": qa})
    liaotian_info.mse = json.dumps(liaotian_mes,ensure_ascii=False, indent=4)
    liaotian_info.save()
    print(liaotian_mes)
    print("最后添加ai回答")
    yield json.dumps(oss)#最后添加ai回答
    yield "\r\n"

ret_data={
                    "error_code": 1,#1失败
                    "reason": "失败，token不存在，请联系购买。",
                    "token":"token",
                    # "balance":balance,
                    "result": {
                        "_signature": "no token"
                    }
                }
import openai


'''
# {"messages":[{"role":"system","content":"IMPORTANT: You are a virtual assistant powered by the gpt-3.5-turbo model, now time is 2023/6/1 18:40:02}"},{"role":"user","content":"我想让你充当Django开发专家。我将提供一些关于python,django等代码问题的具体信息，而你的工作就是想出为我解决问题的策略。这可能包括建议代码、代码逻辑思路策略。我的第一个请求是“Django怎么获取请求头参数”\n"},{"role":"assistant","content":"\n\n访问密码不正确或为空，请前往[设置](/#/settings)页输入正确的访问密码，或者填入你自己的 OpenAI API Key。\n\n```json\n{\n  \"error\": true,\n  \"msg\": \"wrong access code\"\n}\n```"},{"role":"user","content":"6"}],"stream":true,"model":"gpt-3.5-turbo","temperature":0.5,"presence_penalty":0}

'''



import uuid
def chat_process(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps("不支持的访问！"),content_type='application/json')
    if request.method == 'POST':
        try:
            '''
            {"message":"request to https://api.openai.com/v1/chat/completions failed, reason: connect ETIMEDOUT 128.242.240.61:443","data":null,"status":"Fail"}
            
            
            '''

            token = str(request.META.get('HTTP_AUTHORIZATION')).replace("Bearer ","")
            print(token)#获取token

            question_unicode = request.body.decode('utf-8')
            question = json.loads(question_unicode)
            print(question)#获取用户输入
            
            if(token == None or  question ==None):return HttpResponse("出错了...")
            try:
                token_raw =  tokens.objects.get(token=token)#获取token对象
                ret_token = istokenok(token_raw)
                print(ret_token)
                if(ret_token["error_code"] != 0):#异常返回原因
                    token_raw.balance =0 #异常清零
                    token_raw.save()
                    return HttpResponse(mes(ret_token),content_type='application/json')
                token_raw.balance -=1#正常扣点
                token_raw.save()
                log = loging(users = token,mse = json.dumps(question, ensure_ascii=False, indent=4),state="用户提问")
                log.save()
                #判断是否新聊天
                
                if(question["options"] == {} ):#新聊天
                    '''
                    {"prompt":"第一句","options":{},"systemMessage":"You are ChatGPT, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown.","temperature":0.8,"top_p":1}
                    '''
                    liaotian_id =  uuid.uuid4()#id
                    print("新聊天",liaotian_id)#需要创建数据，生成id
                    mesg_liaotian = [
                                {"role":"system","content":question["systemMessage"]},
                                {"role":"user","content":question["prompt"]}
                    ]
                    log = liaotian(uid = liaotian_id,users = token,mse = json.dumps(mesg_liaotian, ensure_ascii=False, indent=4),state="新聊天")
                    log.save()
                else:
                    '''
                    {"prompt":"第二句","options":{"parentMessageId":"chatcmpl-7NAKtSO74Jtx0jCxenNzAzuwzSxM1"},"systemMessage":"You are ChatGPT, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown.","temperature":0.8,"top_p":1}
                    '''
                    print("接着聊天")#这里需要取出对话id，构建对话列表
                    liaotian_id =  question["options"]["parentMessageId"]
                    print(liaotian_id)
                    liaotian_info =  liaotian.objects.get(uid=liaotian_id)#获取token对象
                    liaotian_mes = json.loads(liaotian_info.mse)
                    liaotian_mes.append({"role": "user","content": question["prompt"]})#添加新问题
                    mesg_liaotian = liaotian_mes
                    # print(mesg_liaotian)
                    liaotian_info.mse = json.dumps(liaotian_mes,ensure_ascii=False, indent=4)#保存聊天
                    liaotian_info.save()

                api_key_obj =  user_cookies.objects.get(uid=5)#获取key对象
                api_key = api_key_obj.cookies
                openai.api_key = api_key

                print(api_key)
                print(liaotian_id)
                response = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo",
                            messages=mesg_liaotian[-5:],
                            stream=True,
                            temperature=question["temperature"],
                            presence_penalty=0,
                            
                            )
# TODO 
                print(response)
                ret_x = ret_stem(str(liaotian_id),token,response)
                return StreamingHttpResponse(ret_x, content_type='application/octet-stream')#流式返回
            except Exception as e:
                print(e)
                return HttpResponse(json.dumps(token_raw),content_type='application/json')
        except Exception as e:
                return HttpResponse(e,content_type='application/json')


def  mes(mes):
    return json.dumps({"message":str(mes),"data":None,"status":"Fail"})



def gpt_info(request):
    if request.method == 'GET':
        
        return HttpResponse("不支持的访问",content_type='application/json')
    if request.method == 'POST':
        try:

            token = request.META.get('HTTP_AUTHORIZATION')
            print(token)#获取token

            question_unicode = request.body.decode('utf-8')
            question = json.loads(question_unicode)
            print(question)#获取用户输入
            
            if(token == None or  question ==None):return HttpResponse("出错了...")
            # ret_data={
            #         "error_code": 1,#1失败
            #         "reason": "失败,token不存在,请联系购买。",
            #         "token":token,
            #         # "balance":balance,
            #         "result": {
            #             "_signature": "no token"
            #         }
            #     }

            try:
                token_raw =  tokens.objects.get(token=token)#获取token对象
                ret_token = istokenok(token_raw)
                print(ret_token)
                if(ret_token["error_code"] != 0):#异常返回原因
                    token_raw.balance =0
                    token_raw.save()
                    return HttpResponse(json.dumps(token_raw),content_type='application/json')
                token_raw.balance -=1#正常扣点
                token_raw.save()
                response = openai.ChatCompletion.create(
                            model=question["model"],
                            messages=question["messages"],
                            stream=question["stream"],
                            temperature=question["temperature"],
                            presence_penalty=question["presence_penalty"],
                            
                            )

                # print(response)
                # ret_x = ret_stem(response)
                return StreamingHttpResponse(response, content_type='text/plain')
                
                ans= response["choices"][0]["message"]["content"]
                return   HttpResponse(ans)
            except Exception as e:
                print(e)
                return HttpResponse(json.dumps(token_raw),content_type='application/json')
        except:
                return HttpResponse("出错了...")


def session(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps({"status":"Success","message":"","data":{"auth":True,"model":"ChatGPTAPI"}}),content_type='application/json')
        
    if request.method == 'POST':
        return HttpResponse(json.dumps({"status":"Success","message":"","data":{"auth":True,"model":"ChatGPTAPI"}}),content_type='application/json')

def verify(request):
    '''
    {"status":"Fail","message":"密钥无效 | Secret key is invalid","data":null}
    {"status":"Success","message":"Verify successfully","data":null}
    
    '''
    if request.method == 'GET':
        return HttpResponse(json.dumps({"status":"Success","message":"","data":{"auth":True,"model":"ChatGPTAPI"}}),content_type='application/json')
        
    if request.method == 'POST':
        return HttpResponse(json.dumps({"status":"Success","message":"Verify successfully","data":None}),content_type='application/json')#控制访问权限





def index(request):
    if request.method == 'GET':
        return HttpResponse("Hello, world. You're at the token index.")


    elif request.method == 'POST':
        
    #     try:
    #         url = request.POST.get('url')
    #         body = request.POST.get('body')
    #         token = request.META.get("HTTP_AUTHORIZATION")
    #         # print(token)
    #         ret_data={
    #             "error_code": 1,#1失败
    #             "reason": "失败，token不存在，请联系购买。",
    #             "token":token,
    #             "result": {
    #                 "_signature": "no token"
    #             }
    #         }
    #         try:
    #             token_raw =  tokens.objects.get(token=token)
    #             isok = istokenok(token_raw,ret_data)
    #             if(isok["error_code"] == 0):
    #                 token_raw.Recentime=datetime.datetime.now()
    #                 token_raw.balance -=1
    #                 token_raw.save()
    #                 print("ok")
    #                 body_json_str = json.dumps({i.split("=", maxsplit=1)[0]:i.split("=", maxsplit=1)[1] for i in body.split("&")})
    #                 signature = ctx.call('sign_post', url, body_json_str)
                    
                    
    #                 isok["balance"]=token_raw.balance
    #                 isok["result"]["_signature"]=signature
    #                 log = loging(users = token,mse = json.dumps(isok),state="成功")
    #                 log.save()
    #                 return HttpResponse(json.dumps(isok),content_type='application/json')
    #             else:
    #                 log = loging(users = token,mse = json.dumps(isok),state="失败")
    #                 log.save()
    #                 return HttpResponse(json.dumps(isok),content_type='application/json')
    #         except Exception as e:
    #             ret_data["error_code"]=1#1失败
    #             ret_data["reason"]=f"失败，token不存在，请联系购买,{e}"
    #             log = loging(users = token,mse = json.dumps(ret_data),state="失败")
    #             log.save()
    #             return HttpResponse(json.dumps(ret_data),content_type='application/json')

    #     except Exception as e:
    #         #  HttpResponse()
    #         return HttpResponse(json.dumps({
    #             "error_code": 1,
    #             "reason": e
    #         }), content_type='application/json')
    #     # return HttpResponse('欢迎你：%s,请牢记你的密码%s' %(name,pwd))
    # else:
        return HttpResponse('收到灵异请求')

def addlogin(request):
    if request.method == 'GET':
        return render(request, 'tokenapps/index.html')
        # return HttpResponse("Hello, world. You're at the cookies index.")
    elif request.method == 'POST':
        mse = request.POST.get('mse')
        users = request.POST.get('users')
        state = request.POST.get('state')
        try:
            log = loging(users = users,mse = json.dumps(json.loads(mse) , sort_keys=True, indent=4,ensure_ascii=False ,separators=(',', ':')),state=state)
            log.save()
        except:
            log = loging(users = users,mse = mse,state=state)
            log.save()
        return HttpResponse(json.dumps({"code":"ok","time":time.time()}),content_type='application/json')

# mse = 
# users 
# state 

def cookies(request):
    if request.method == 'GET':
        return render(request, 'tokenapps/index.html')
        # return HttpResponse("Hello, world. You're at the cookies index.")
    elif request.method == 'POST':

        return HttpResponse("Hello, world. You're at the cookies index.")
