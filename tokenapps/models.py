from django.db import models
import datetime
# Create your models here.
from django.db import models
import django.utils.timezone as timezone
'''
2023年6月3日
聊天表
'''






class tokens(models.Model):
    token = models.CharField("令牌",max_length=200,primary_key=True)
    creatime = models.DateTimeField("创建时间",default=datetime.datetime.now())#创建时间
    Recentime=models.DateTimeField("最近登录时间",default=datetime.datetime.now())#最近登录时间
    balance = models.IntegerField("余额",default=10)#余额
    purchasetime=models.DateTimeField("购买时间",default=datetime.datetime.now())#购买时间
    timelength  = models.IntegerField("时长(秒)",default=3600)#时长：秒，默认一小时过期
    remark = models.CharField("备注",max_length=200,default="备注")#备注
    isBanned = models.BooleanField("是否封禁",default=False)#是否封禁
    class Meta:         
        # 表备注        
        verbose_name = "令牌表"

class user_admin(models.Model):
    username = models.CharField("用户名",max_length=200,primary_key=True)#用户名
    password = models.CharField("密码",max_length=200)#密码
    creatime = models.DateTimeField("创建时间",default=datetime.datetime.now())#创建时间
    Recentime=models.DateTimeField("最近登录时间",default=datetime.datetime.now())#最近登录时间
    uses = models.IntegerField("权限使用次数",default=0)#使用次数
    class Meta:         
        # 表备注        
        verbose_name = "管理员表"

class loging(models.Model):
    uid =  models.AutoField("id",primary_key=True) #id
    creatime = models.DateTimeField("创建时间",default=datetime.datetime.now())#创建时间
    mse = models.CharField("内容",max_length=200,default="默认内容")#内容
    users = models.CharField("用户名/token",max_length=200,default="默认用户名")#用户名/token
    state = models.CharField("状态",max_length=200,default="默认状态")#状态
    class Meta:         
        # 表备注        
        verbose_name = "日志表"

class liaotian(models.Model):
    uid =  models.CharField("UUID",max_length=200,primary_key=True)#用户名
    creatime = models.DateTimeField("创建时间",default=datetime.datetime.now())#创建时间
    mse = models.CharField("内容",max_length=200,default="默认内容")#内容
    users = models.CharField("用户名/token",max_length=200,default="默认用户名")#用户名/token
    state = models.CharField("状态",max_length=200,default="默认状态")#状态
    class Meta:         
        # 表备注        
        verbose_name = "聊天表"



class user_cookies(models.Model):
    uid = models.AutoField("id",primary_key=True) #iddefault=datetime.datetime.now()
    creatime = models.DateTimeField("创建时间",default=datetime.datetime.now())#创建时间
    cookies = models.CharField("内容",max_length=100000)#内容
    state = models.CharField("状态",max_length=200)#状态
    class Meta:         
        # 表备注        
        verbose_name = "cookies表"




