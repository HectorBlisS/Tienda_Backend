from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_social_oauth2 import urls as socialUrls


from rest_framework import routers
from products.views import ProductsViewsets
from orders.views import OrderViewSet


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include(socialUrls))
    #url(r'^mensajes', include(apiUrls))
]

router = routers.DefaultRouter()
router.register(r'products', ProductsViewsets)
router.register(r'orders', OrderViewSet)

urlpatterns += router.urls
