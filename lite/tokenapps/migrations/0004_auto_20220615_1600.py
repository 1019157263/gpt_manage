# Generated by Django 3.2.13 on 2022-06-15 08:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokenapps', '0003_auto_20220615_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokens',
            name='jixing',
            field=models.CharField(default='默认未填写', max_length=200, verbose_name='机型'),
        ),
        migrations.AlterField(
            model_name='loging',
            name='creatime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 16, 0, 44, 153662), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='tokens',
            name='Recentime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 16, 0, 44, 105844), verbose_name='最近登录时间'),
        ),
        migrations.AlterField(
            model_name='tokens',
            name='creatime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 16, 0, 44, 105844), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='tokens',
            name='purchasetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 16, 0, 44, 105844), verbose_name='购买时间'),
        ),
        migrations.AlterField(
            model_name='user_admin',
            name='Recentime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 16, 0, 44, 153159), verbose_name='最近登录时间'),
        ),
        migrations.AlterField(
            model_name='user_admin',
            name='creatime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 16, 0, 44, 153159), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='user_cookies',
            name='creatime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 16, 0, 44, 154165), verbose_name='创建时间'),
        ),
    ]