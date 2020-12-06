from django.contrib import admin
from xb_paper import models


# Register your models here.
@admin.register(models.Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_on', 'time', 'get_categories')
    list_per_page = 15
    list_filter = ('categories',)
    filter_horizontal = ('categories', 'researchers')
    search_fields = ('title', 'publish_on', 'time', 'categories__name_en', 'categories__name_zh')

    def get_categories(self, obj):
        return ''.join([str(item) + ';' for item in obj.categories.all().iterator()])

    get_categories.short_description = 'Categories'


@admin.register(models.Researcher)
class ResearcherAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'email')
    list_per_page = 15
    search_fields = ('name', 'organization', 'email')


@admin.register(models.PaperCategory)
class PaperCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_zh')
    list_per_page = 15
