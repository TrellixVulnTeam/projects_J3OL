# Generated by Django 2.2.3 on 2019-11-06 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_conditioninfo_logininfo_medicineinfo_usertoken'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserToken',
        ),
    ]
