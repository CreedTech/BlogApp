from django.contrib import admin

from .models import Blog, Category
from import_export.admin import ImportExportMixin

# Register your models here.

class BlogAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ["title", "created_at"]

admin.site.register(Blog, BlogAdmin)

class CategoryAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ["name"]
admin.site.register(Category, CategoryAdmin)
