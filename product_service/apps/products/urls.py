from django.urls import path, include

app_name = 'products'

urlpatterns = [
    path('products/', include('apps.products.urls.productUrls')),
    path('categories/', include('apps.products.urls.categoryUrls')),
]
