# Generated by Django 2.2 on 2020-12-06 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xb_paper', '0008_auto_20201206_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='title_zh',
        ),
    ]
