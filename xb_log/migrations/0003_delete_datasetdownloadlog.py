# Generated by Django 2.2 on 2020-12-06 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xb_log', '0002_accesslog_path'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DatasetDownloadLog',
        ),
    ]
