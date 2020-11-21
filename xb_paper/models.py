from django.db import models


# Create your models here.
class Researcher(models.Model):
    organization = models.CharField(max_length=1024)
    name = models.CharField(max_length=1024)

    class Meta:
        db_table = 'Researcher'


class PaperCategory(models.Model):
    name_zh = models.CharField(max_length=1024)
    name_en = models.CharField(max_length=1024)

    class Meta:
        db_table = 'PaperCategory'


class Paper(models.Model):
    title = models.CharField(max_length=1024)
    publish_on = models.CharField(max_length=1024)
    time = models.DateTimeField()
    page = models.CharField(max_length=128)
    bibTex = models.CharField(max_length=1024)
    categories = models.ManyToManyField('xb_paper.PaperCategory')
    researchers = models.ManyToManyField('xb_paper.Researcher')

    class Meta:
        db_table = 'Paper'

