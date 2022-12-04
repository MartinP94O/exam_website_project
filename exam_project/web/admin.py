from django.contrib import admin

from exam_project.web.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
