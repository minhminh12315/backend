
from django.contrib import admin
from django.urls import path
from apps.products.views.productViews import GetVariantBySku, GetAllVariantView,GetRecommandProductsView

urlpatterns = [
    path('list_products', GetAllVariantView.as_view(), name='get_all_products'),
    path('recommand_products', GetRecommandProductsView.as_view(), name='get_recommand_products'),
    path('get_product/<str:sku>', GetVariantBySku.as_view(), name='get_product_by_sku'),
]
