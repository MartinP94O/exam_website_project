from django.contrib import admin

from exam_project.web.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('product_price', 'product_type', 'product_model',)
    list_display = ('product_model', 'product_model', 'product_price', 'product_year')
    search_fields = ('product_price', 'product_type', 'product_model', 'product_year')


