# Generated by Django 2.2 on 2020-12-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xb_dataset', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='cite_ACM',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataset',
            name='cite_IEEE',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataset',
            name='cite_bibTex',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
