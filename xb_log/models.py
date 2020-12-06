from django.db import models
from django.utils import timezone


# Create your models here.
class AccessLog(models.Model):
    ip = models.CharField(max_length=128)
    path = models.CharField(max_length=128)
    referer = models.CharField(max_length=1024, null=True)
    time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'AccessLog'
        verbose_name = verbose_name_plural = '访问日志'

    def __str__(self):
        return '%s:%s' % (self.path, self.ip)
