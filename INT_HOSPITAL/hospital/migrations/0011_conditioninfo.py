# Generated by Django 2.2.3 on 2019-11-09 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_delete_conditioninfo'),
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
                ('condition', models.CharField(max_length=255, verbose_name='患者病况')),
            ],
            options={
                'verbose_name': '病况信息',
                'verbose_name_plural': '病况信息',
            },
        ),
    ]
