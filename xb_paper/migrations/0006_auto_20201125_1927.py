# Generated by Django 2.2 on 2020-11-25 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xb_paper', '0005_researcher_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researcher',
            name='email',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='image',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
