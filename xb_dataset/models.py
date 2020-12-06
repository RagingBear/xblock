from django.db import models


# Create your models here.
class Dataset(models.Model):
    name_zh = models.CharField(max_length=1024)
    name_en = models.CharField(max_length=1024)
    introduction_zh = models.TextField()
    introduction_en = models.TextField()
    url = models.CharField(max_length=1024)
    cite_bibTex = models.TextField()
    cite_ACM = models.TextField()
    cite_IEEE = models.TextField()
    paper = models.OneToOneField('xb_paper.Paper', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'Dataset'
        verbose_name = verbose_name_plural = '数据集'

    def __str__(self):
        return '%s(%s)' % (self.name_en, self.name_zh)


class DatasetFile(models.Model):
    name = models.CharField(max_length=1024)
    introduction_zh = models.TextField()
    introduction_en = models.TextField()
    sample = models.TextField()
    dataset = models.ForeignKey('xb_dataset.Dataset', on_delete=models.CASCADE)

    class Meta:
        db_table = 'DatasetFile'
        verbose_name = verbose_name_plural = '数据集文件'

    def __str__(self):
        return '%s:%s(%s)' % (self.name, self.dataset.name_en, self.dataset.name_zh)
