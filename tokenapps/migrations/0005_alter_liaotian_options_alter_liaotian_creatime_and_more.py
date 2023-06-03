# Generated by Django 4.2.1 on 2023-06-03 02:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokenapps', '0004_alter_liaotian_creatime_alter_loging_creatime_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='liaotian',
            options={'verbose_name': '聊天表'},
        ),
        migrations.AlterField(
            model_name='liaotian',
            name='creatime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 10, 33, 47, 376982), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='loging',
            name='creatime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 10, 33, 47, 376982), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='tokens',
            name='Recentime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 10, 33, 47, 356144), verbose_name='最近登录时间'),
        ),
        migrations.AlterField(
            model_name='tokens',
            name='creatime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 10, 33, 47, 356144), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='tokens',
            name='purchasetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 10, 33, 47, 356144), verbose_name='购买时间'),
        ),
        migrations.AlterField(
            model_name='user_admin',
            name='Recentime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 10, 33, 47, 376982), verbose_name='最近登录时间'),
        ),
        migrations.AlterField(
            model_name='user_admin',
            name='creatime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 10, 33, 47, 376982), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='user_cookies',
            name='creatime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 10, 33, 47, 376982), verbose_name='创建时间'),
        ),
    ]
