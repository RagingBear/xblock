from django.contrib import admin
from xb_dataset import models

# Register your models here.
admin.site.register(models.Dataset)
admin.site.register(models.DatasetFileColumn)
admin.site.register(models.DatasetFile)
