from django.db import models


# Create your models here.
class Dataset(models.Model):
    name_zh = models.CharField(max_length=1024, verbose_name='数据集名称')
    name_en = models.CharField(max_length=1024, verbose_name='Dataset name')
    introduction_zh = models.TextField(verbose_name='简介')
    introduction_en = models.TextField(verbose_name='introduction')
    url = models.CharField(max_length=1024, verbose_name='下载链接')
    cite_bibTex = models.TextField()
    cite_ACM = models.TextField()
    cite_IEEE = models.TextField()
    paper = models.OneToOneField('xb_paper.Paper', on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name='对应论文')

    class Meta:
        db_table = 'Dataset'
        verbose_name = verbose_name_plural = '数据集'

    def __str__(self):
        return '%s(%s)' % (self.name_en, self.name_zh)


class DatasetFile(models.Model):
    name = models.CharField(max_length=1024, verbose_name='数据文件名称')
    introduction_zh = models.TextField(verbose_name='简介')
    introduction_en = models.TextField(verbose_name='introduction')
    sample = models.TextField(verbose_name='样例(JSON格式)')
    dataset = models.ForeignKey('xb_dataset.Dataset', on_delete=models.CASCADE, verbose_name='对应数据集')

    class Meta:
        db_table = 'DatasetFile'
        verbose_name = verbose_name_plural = '数据集文件'

    def __str__(self):
        return '%s:%s(%s)' % (self.name, self.dataset.name_en, self.dataset.name_zh)
