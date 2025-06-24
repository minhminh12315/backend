from django.contrib import admin
from .models import Category, Product, Variant, Invoice, InvoiceItem
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at', 'updated_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    
class VariantAdmin(admin.ModelAdmin):
    list_display = ('sku', 'product','category_name', 'price', 'stock', 'volume', 'created_at', 'updated_at')
    search_fields = ('sku', 'product__name', 'volume')
    list_filter = ('product',)
    
    def category_name(self, obj):
        return obj.product.category.name if obj.product.category else 'No Category'
    category_name.short_description = 'Category Name'
    
class InvoiceItemInline(admin.ModelAdmin):
    list_display = ('invoice', 'variant','sku', 'quantity', 'totalPrice')
    def sku(self, obj):
        return obj.variant.sku if obj.variant else 'No SKU'
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Variant,VariantAdmin)
admin.site.register(Invoice)
admin.site.register(InvoiceItem,InvoiceItemInline)