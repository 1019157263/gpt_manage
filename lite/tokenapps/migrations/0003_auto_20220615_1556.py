# Generated by Django 3.2.13 on 2022-06-15 07:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokenapps', '0002_auto_20210820_1612'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loging',
            options={'verbose_name': '日志表'},
        ),
        migrations.AlterModelOptions(
            name='tokens',
            options={'verbose_name': '令牌表'},
        ),
        migrations.AlterModelOptions(
            name='user_admin',
            options={'verbose_name': '管理员表'},
        ),
        migrations.AlterModelOptions(
            name='user_cookies',
            options={'verbose_name': 'cookies表'},
        ),
        migrations.AddField(
            model_name='tokens',
            name='usenum',
            field=models.IntegerField(default=0, verbose_name='调用次数'),
        ),
        migrations.AlterField(
            model_name='loging',
            name='creatime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 15, 56, 19, 175961), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='tokens',
            name='Recentime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 15, 56, 19, 122475), verbose_name='最近登录时间'),
        ),
        migrations.AlterField(
            model_name='tokens',
            name='creatime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 15, 56, 19, 122475), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='tokens',
            name='purchasetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 15, 56, 19, 122475), verbose_name='购买时间'),
        ),
        migrations.AlterField(
            model_name='user_admin',
            name='Recentime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 15, 56, 19, 175961), verbose_name='最近登录时间'),
        ),
        migrations.AlterField(
            model_name='user_admin',
            name='creatime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 15, 56, 19, 175961), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='user_cookies',
            name='creatime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 15, 56, 19, 176464), verbose_name='创建时间'),
        ),
    ]