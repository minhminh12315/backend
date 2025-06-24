from apps.products.models import Category
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status,filters
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from apps.products.serializers.Category.categorySerializers import CategorySerializer

class GetCategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    authentication_classes = []
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        response = {
            'status': 200,
            'message': 'Categories retrieved successfully',
            'code':"SUCCESS",
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    
class GetProductInCategoryView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response = {
            'status': 200,
            'message': 'Category retrieved successfully',
            'code': "SUCCESS",
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)