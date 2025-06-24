from django.urls import path, include

urlpatterns = []

# Import từng module và nối vào urlpatterns
from . import categoryUrls, productUrls

urlpatterns += categoryUrls.urlpatterns
urlpatterns += productUrls.urlpatterns