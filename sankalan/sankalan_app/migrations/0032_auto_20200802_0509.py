# Generated by Django 3.0.3 on 2020-08-02 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sankalan_app', '0031_auto_20200802_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aadhaar_data',
            name='email',
            field=models.EmailField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='aadhaar_data',
            name='mobile_no',
            field=models.IntegerField(default='00'),
        ),
    ]
