
from django.contrib import admin
from django.urls import path
from apps.products.views.categoryViews import GetCategoryView,GetProductInCategoryView

urlpatterns = [
    path('category', GetCategoryView.as_view(), name='get_category'),
    path('category/<int:pk>', GetProductInCategoryView.as_view(), name='get_products_category'),

]
