from django.contrib import admin
from django.contrib.admin import SimpleListFilter, ModelAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from exam_project.accounts.forms import UserCreateForm, UserEditForm
from exam_project.web.models import Product

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    form = UserEditForm
    add_form = UserCreateForm
    list_filter = ('first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active',)
    list_display_links = ('first_name', 'last_name')



