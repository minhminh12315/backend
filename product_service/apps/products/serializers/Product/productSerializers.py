from rest_framework.serializers import ModelSerializer, SerializerMethodField
from apps.products.models import Category, Product, Variant

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "category", "created_at", "updated_at"]
        read_only_fields = ['created_at', 'updated_at']
class VariantSerializer(ModelSerializer):
    category_name = SerializerMethodField()
    class Meta:
        model = Variant
        fields = ["id", "sku", "product", "price", "stock", "volume", "image", "category_name", "created_at", "updated_at"]
        read_only_fields = ['created_at', 'updated_at']

    def get_category_name(self, obj):
        return obj.product.category.name if obj.product.category else 'No Category'
    