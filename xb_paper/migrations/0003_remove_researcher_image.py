# Generated by Django 2.2 on 2020-11-25 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xb_paper', '0002_auto_20201125_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researcher',
            name='image',
        ),
    ]