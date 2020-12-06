from django.db import models


# Create your models here.
class Researcher(models.Model):
    organization = models.CharField(max_length=1024)
    name = models.CharField(max_length=1024)
    image = models.FileField(default='#', null=True)
    email = models.CharField(max_length=128, default='', null=True)

    class Meta:
        db_table = 'Researcher'
        verbose_name = verbose_name_plural = '论文作者'

    def __str__(self):
        return self.name


class PaperCategory(models.Model):
    name_zh = models.CharField(max_length=1024)
    name_en = models.CharField(max_length=1024)

    class Meta:
        db_table = 'PaperCategory'
        verbose_name = verbose_name_plural = '论文类别'

    def __str__(self):
        return '%s(%s)' % (self.name_en, self.name_zh)


class Paper(models.Model):
    title = models.CharField(max_length=1024)
    publish_on = models.CharField(max_length=1024)
    time = models.DateField()
    bibTex = models.TextField()
    categories = models.ManyToManyField('xb_paper.PaperCategory')
    researchers = models.ManyToManyField('xb_paper.Researcher')

    class Meta:
        db_table = 'Paper'
        verbose_name = verbose_name_plural = '论文'

    def __str__(self):
        return self.title
