from django.contrib import admin
from .models import Category, Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "category", "description", "image", "count")
    list_display_links = ("title", "category", "description", "image")
    list_editable = ("count", "price")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
