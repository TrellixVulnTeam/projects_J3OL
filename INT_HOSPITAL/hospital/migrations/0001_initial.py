# Generated by Django 2.2.3 on 2019-11-04 23:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConditionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pname', models.CharField(blank=True, max_length=50, null=True, verbose_name='患者名字')),
                ('Psex', models.CharField(choices=[('girl', '女'), ('boy', '男')], default='girl', max_length=50, verbose_name='患者性别')),
                ('Page', models.IntegerField(verbose_name='患者年龄')),
                ('Phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='患者电话')),
                ('Psfz', models.CharField(blank=True, max_length=50, null=True, verbose_name='患者身份证')),
                ('Money', models.IntegerField(blank=True, null=True, verbose_name='医药费')),
                ('Adds', models.CharField(blank=True, max_length=200, null=True, verbose_name='患者地址')),
                ('blood', models.CharField(blank=True, max_length=50, null=True, verbose_name='患者血型')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('condition', models.CharField(max_length=50, verbose_name='患者病况')),
            ],
            options={
                'verbose_name': '病况信息',
                'verbose_name_plural': '病况信息',
            },
        ),
        migrations.CreateModel(
            name='LoginInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uid', models.IntegerField(verbose_name='登录者ID')),
                ('Pwd', models.CharField(max_length=50, verbose_name='登录密码')),
                ('Uname', models.CharField(blank=True, max_length=50, null=True, verbose_name='姓名')),
                ('Sex', models.CharField(choices=[('girl', '女'), ('boy', '男'), ('unknown', '未知')], default='unknown', max_length=50, verbose_name='性别')),
                ('Age', models.IntegerField(verbose_name='年龄')),
                ('Identity', models.CharField(choices=[('registration', '挂号'), ('doctor', '医生')], default='patient', max_length=50, verbose_name='类型')),
                ('Office', models.CharField(blank=True, max_length=50, null=True, verbose_name='科室')),
                ('stata', models.IntegerField(blank=True, null=True)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '登录信息',
                'verbose_name_plural': '登录信息',
            },
        ),
        migrations.CreateModel(
            name='MedicineInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pmedid', models.CharField(max_length=50, verbose_name='编号')),
                ('Pmedname', models.CharField(max_length=50, verbose_name='编号')),
                ('Pchangjia', models.CharField(max_length=50, verbose_name='编号')),
                ('Pdate', models.CharField(max_length=50, verbose_name='编号')),
                ('bzq', models.CharField(max_length=50, verbose_name='编号')),
                ('using', models.CharField(max_length=50, verbose_name='编号')),
                ('size', models.CharField(max_length=50, verbose_name='编号')),
                ('inprice', models.CharField(max_length=50, verbose_name='编号')),
                ('outprice', models.CharField(max_length=50, verbose_name='编号')),
                ('stuffid', models.IntegerField(blank=True, null=True, verbose_name='员工编号')),
                ('userid', models.IntegerField(blank=True, null=True, verbose_name='客户编号')),
            ],
        ),
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pid', models.IntegerField(verbose_name='患者ID')),
                ('Pname', models.CharField(blank=True, max_length=50, null=True, verbose_name='患者名字')),
                ('Psex', models.CharField(choices=[('girl', '女'), ('boy', '男')], default='girl', max_length=50, verbose_name='患者性别')),
                ('Page', models.IntegerField(verbose_name='患者年龄')),
                ('Phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='患者电话')),
                ('Psfz', models.CharField(blank=True, max_length=50, null=True, verbose_name='患者身份证')),
                ('Money', models.IntegerField(blank=True, null=True, verbose_name='医药费')),
                ('Adds', models.CharField(blank=True, max_length=200, null=True, verbose_name='用户地址')),
                ('Identity', models.CharField(choices=[('patient', '患者'), ('doctor', '医生')], default='patient', max_length=50, verbose_name='用户类型')),
                ('blood', models.CharField(blank=True, max_length=50, null=True, verbose_name='用户血型')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '患者信息',
                'verbose_name_plural': '患者信息',
            },
        ),
    ]
