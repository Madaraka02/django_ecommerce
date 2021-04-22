from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Shipping)

class  CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_tag')
admin.site.register(Category, CategoryAdmin)    

class  ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'color_code', 'color_bg')
admin.site.register(Color, ColorAdmin)

class  ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'status','size', 'color', 'price', 'brand', 'category', 'is_featured')
    list_editable = ('name', 'status', 'size', 'price', 'color', 'is_featured')
admin.site.register(Product, ProductAdmin)

class  AdvertAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_editable = ('title',)
admin.site.register(Advert, AdvertAdmin)

class  ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag', 'product', 'color', 'size')
    list_editable=('color', 'size')
admin.site.register(ProductAttribute, ProductAttributeAdmin)