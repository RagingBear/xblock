# Generated by Django 2.2 on 2020-12-06 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xb_dataset', '0005_remove_datasetfile_name_zh'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datasetfile',
            old_name='name_en',
            new_name='name',
        ),
    ]