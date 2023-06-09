# Generated by Django 4.2.1 on 2023-06-03 02:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokenapps', '0002_auto_20210820_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='liaotian',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('creatime', models.DateTimeField(default=datetime.datetime(2023, 6, 3, 10, 28, 17, 911008), verbose_name='创建时间')),
                ('mse', models.CharField(default='默认内容', max_length=200, verbose_name='内容')),
                ('users', models.CharField(default='默认用户名', max_length=200, verbose_name='用户名/token')),
                ('state', models.CharField(default='默认状态', max_length=200, verbose_name='状态')),
            ],
            options={
                'verbose_name': '日志表',
            },
        ),
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
        migrations.AlterField(
            model_name='loging',
            name='creatime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 10, 28, 17, 911008), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='tokens',
            name='Recentime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 10, 28, 17, 879758), verbose_name='最近登录时间'),
        ),
        migrations.AlterField(
            model_name='tokens',
            name='creatime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 10, 28, 17, 879758), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='tokens',
            name='purchasetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 10, 28, 17, 879758), verbose_name='购买时间'),
        ),
        migrations.AlterField(
            model_name='user_admin',
            name='Recentime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 10, 28, 17, 911008), verbose_name='最近登录时间'),
        ),
        migrations.AlterField(
            model_name='user_admin',
            name='creatime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 10, 28, 17, 911008), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='user_cookies',
            name='creatime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 10, 28, 17, 911008), verbose_name='创建时间'),
        ),
    ]
