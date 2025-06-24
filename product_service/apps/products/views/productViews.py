from apps.products.models import Category, Product, Variant
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status,filters
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from apps.products.serializers.Product.productSerializers import ProductSerializer,VariantSerializer
from itertools import groupby
from django.db.models import Count, Avg, Sum
from apps.products.filters import ProductFilter

class GetAllVariantView(ListAPIView):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer
    permission_classes = [AllowAny]
    authentication_classes = []
    filterset_class = ProductFilter
    def get_queryset(self):
        allVariants = Variant.objects.all().select_related('product__category').order_by('product__category__name')
        return allVariants

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        response = {
            'status': 200,
            'message': 'Variants retrieved successfully',
            'code': "SUCCESS",
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
class GetRecommandProductsView(ListAPIView):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def get_queryset(self):
        recommandProducts = Variant.objects.annotate(total_quantity=Sum('items__quantity')).filter(total_quantity__gt=0).order_by('-total_quantity')[:2]
        return recommandProducts

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        response = {
            'status': 200,
            'message': 'Products retrieved successfully',
            'code': "SUCCESS",
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)