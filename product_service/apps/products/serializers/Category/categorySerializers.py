from rest_framework.serializers import ModelSerializer, SerializerMethodField
from apps.products.models import Category, Product, Variant
from apps.products.serializers.Product.productSerializers import ProductSerializer

class CategorySerializer(ModelSerializer):
    products = SerializerMethodField()
    class Meta:
        model = Category
        fields = ["id", "name", "description", "products", "created_at", "updated_at"]
        read_only_fields = ['created_at', 'updated_at']
        
    def get_products(self, obj):
        products = Product.objects.filter(category=obj)
        return ProductSerializer(products, many=True).data