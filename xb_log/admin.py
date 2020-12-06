from django.contrib import admin
from xb_log import models


# Register your models here.
@admin.register(models.AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('ip', 'path', 'time', 'referer', 'time')
    list_display_links = None
    search_fields = ('ip', 'path', 'time', 'referer', 'time')
