# Generated by Django 3.2.6 on 2021-08-20 02:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loging',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('creatime', models.DateTimeField(verbose_name='date published')),
                ('mse', models.CharField(default='默认内容', max_length=200)),
                ('users', models.CharField(default='默认用户名', max_length=200)),
                ('state', models.CharField(default='默认状态', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tokens',
            fields=[
                ('token', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('creatime', models.DateTimeField(default=django.utils.timezone.now)),
                ('Recentime', models.DateTimeField(default=django.utils.timezone.now)),
                ('balance', models.IntegerField(default=10)),
                ('purchasetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('timelength', models.IntegerField(default=3600)),
                ('remark', models.CharField(default='备注', max_length=200)),
                ('isBanned', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='user_admin',
            fields=[
                ('username', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=200)),
                ('creatime', models.DateTimeField(default=django.utils.timezone.now)),
                ('Recentime', models.DateTimeField(default=django.utils.timezone.now)),
                ('uses', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='user_cookies',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('creatime', models.DateTimeField(default=django.utils.timezone.now)),
                ('cookies', models.CharField(max_length=100000)),
                ('state', models.CharField(max_length=200)),
            ],
        ),
    ]
