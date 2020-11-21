from django.contrib import admin
from xb_paper import models

# Register your models here.
admin.site.register(models.Paper)
admin.site.register(models.Researcher)
admin.site.register(models.PaperCategory)
