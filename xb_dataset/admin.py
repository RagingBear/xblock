from django.contrib import admin
from xb_dataset import models


# Register your models here.
@admin.register(models.Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_zh', 'url', 'paper')
    search_fields = ('name_en', 'name_zh', 'url', 'paper__title')


@admin.register(models.DatasetFile)
class DatasetFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'dataset',)
    search_fields = ('name', 'dataset__name_en', 'dataset__name_zh')
