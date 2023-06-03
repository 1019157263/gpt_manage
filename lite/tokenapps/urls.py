from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('isOk', views.isok, name='index'),
    path('isok_token', views.isok_token, name='index'),

    path('cookies', views.cookies, name='cookies'),
    path('log', views.addlogin, name='log'),

]