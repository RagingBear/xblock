# Generated by Django 2.2 on 2020-11-25 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaperCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_zh', models.CharField(max_length=1024)),
                ('name_en', models.CharField(max_length=1024)),
            ],
            options={
                'db_table': 'PaperCategory',
            },
        ),
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=1024)),
                ('name', models.CharField(max_length=1024)),
                ('image', models.CharField(max_length=1024)),
            ],
            options={
                'db_table': 'Researcher',
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('publish_on', models.CharField(max_length=1024)),
                ('time', models.DateTimeField()),
                ('page', models.CharField(max_length=128)),
                ('bibTex', models.CharField(max_length=1024)),
                ('categories', models.ManyToManyField(to='xb_paper.PaperCategory')),
                ('researchers', models.ManyToManyField(to='xb_paper.Researcher')),
            ],
            options={
                'db_table': 'Paper',
            },
        ),
    ]