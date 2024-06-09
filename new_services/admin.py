from django.contrib import admin

from .models import NewAPI


@admin.register(NewAPI)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"name": ("name",)}
