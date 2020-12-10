from django.db import models


# Create your models here.
class Researcher(models.Model):
    organization = models.CharField(max_length=1024, verbose_name='组织')
    name = models.CharField(max_length=1024, verbose_name='姓名')
    image = models.FileField(blank=True, null=True, verbose_name='头像')
    email = models.CharField(max_length=128, blank=True, null=True, verbose_name='邮箱')

    class Meta:
        db_table = 'Researcher'
        verbose_name = verbose_name_plural = '论文作者'

    def __str__(self):
        return self.name


class PaperCategory(models.Model):
    name_zh = models.CharField(max_length=1024, verbose_name='分类名称')
    name_en = models.CharField(max_length=1024, verbose_name='category name')

    class Meta:
        db_table = 'PaperCategory'
        verbose_name = verbose_name_plural = '论文类别'

    def __str__(self):
        return self.name_zh
        # return '%s(%s)' % (self.name_en, self.name_zh)


class Paper(models.Model):
    title = models.CharField(max_length=1024, verbose_name='标题')
    publish_on = models.CharField(max_length=1024, verbose_name='发表于')
    time = models.DateField(verbose_name='时间')
    bibTex = models.TextField()
    categories = models.ManyToManyField('xb_paper.PaperCategory', verbose_name='论文类别')
    researchers = models.ManyToManyField('xb_paper.Researcher', verbose_name='作者')

    class Meta:
        db_table = 'Paper'
        verbose_name = verbose_name_plural = '论文'

    def __str__(self):
        return self.title
