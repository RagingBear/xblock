from django.db import models


# Create your models here.
class Dataset(models.Model):
    name_zh = models.CharField(max_length=1024)
    name_en = models.CharField(max_length=1024)
    introduction_zh = models.TextField()
    introduction_en = models.TextField()
    url = models.CharField(max_length=1024)
    cite_bibTex = models.CharField(max_length=1024, null=True)
    cite_ACM = models.CharField(max_length=1024, null=True)
    cite_IEEE = models.CharField(max_length=1024, null=True)
    paper = models.OneToOneField('xb_paper.Paper', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'Dataset'


class DatasetFile(models.Model):
    introduction_zh = models.TextField()
    introduction_en = models.TextField()
    sample = models.TextField()
    dataset = models.ForeignKey('xb_dataset.Dataset', on_delete=models.CASCADE)
    Columns = models.ManyToManyField('xb_dataset.DatasetFileColumn')

    class Meta:
        db_table = 'DatasetFile'


class DatasetFileColumn(models.Model):
    key = models.CharField(max_length=128)
    introduction_zh = models.TextField()
    introduction_en = models.TextField()

    class Meta:
        db_table = 'DatasetFileColumn'
