from django.contrib import admin

from exam_project.web.models import Product


@admin.register(Product)
class PetAdmin(admin.ModelAdmin):
    pass
