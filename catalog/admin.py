from django.contrib import admin

from catalog.models import Category,Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','category_name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name','price','category')

