from django.contrib import admin

from .models import Menu, MenuItem

# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display =  ("pk", "name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "parent", "menu", "slug")
    prepopulated_fields = {"slug": ("title",)}


