# Generated by Django 2.2 on 2020-11-25 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xb_paper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researcher',
            name='image',
            field=models.CharField(max_length=512),
        ),
    ]