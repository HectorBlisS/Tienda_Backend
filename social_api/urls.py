from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_social_oauth2 import urls as socialUrls


from rest_framework import routers
from products.views import ProductsViewsets
from orders.views import OrderViewSet

from django.views.static import serve
from django.conf import settings

from products import urls as productUrls

#frase
from phrases.views import FraseView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include(socialUrls)),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}
        ),
    url(r'^extra/', include(productUrls)),
    url(r'^frase/$', FraseView.as_view(), name="frase")
    #url(r'^mensajes', include(apiUrls))
]

router = routers.DefaultRouter()
router.register(r'products', ProductsViewsets)
router.register(r'orders', OrderViewSet)

urlpatterns += router.urls
