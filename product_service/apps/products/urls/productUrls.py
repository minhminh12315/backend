
from django.contrib import admin
from django.urls import path
from apps.products.views.productViews import GetAllVariantView,GetRecommandProductsView

urlpatterns = [
    path('list_products', GetAllVariantView.as_view(), name='get_all_products'),
    path('recommand_products', GetRecommandProductsView.as_view(), name='get_recommand_products'),
]
