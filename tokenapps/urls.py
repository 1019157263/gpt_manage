from django.urls import path

from . import views
"gpt_info"
"chat-process"
'''
http://127.0.0.1:3002/verify

'''
urlpatterns = [
    path('', views.index, name='index'),
    path('isOk', views.isok, name='index'),
    path('gpt_info', views.gpt_info, name='index'),
    path('session', views.session, name='index'),
    path('chat-process', views.chat_process, name='index'),
    path('verify', views.verify, name='index'),
    
    
    
    path('cookies', views.cookies, name='cookies'),
    path('log', views.addlogin, name='log'),

]