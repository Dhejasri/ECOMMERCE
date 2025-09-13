from django.contrib import admin
from .models import Product , ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3 


@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline] 
    list_filter = ('category',)
    list_display = ('id','name','price','category')
    search_fields = ('name','category')



