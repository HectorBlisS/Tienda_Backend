from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_social_oauth2 import urls as socialUrls


from rest_framework import routers
from products.views import ProductsViewsets
from orders.views import OrderViewSet, OrderAndPay

from django.views.static import serve
from django.conf import settings

from products import urls as productUrls

#frase
from phrases.views import FraseView

#accounts
from accounts import urls as accountsUrls
#coupons
from coupons import urls as couponsUrls

#storage
from cloud_storage.views import GetSignedUrl

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include(socialUrls)),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}
        ),
    url(r'^extra/', include(productUrls)),
    url(r'^frase/$', FraseView.as_view(), name="frase"),
    url(r'^pay/$', OrderAndPay.as_view()),
    url(r'^accounts/', include(accountsUrls)),
    url(r'^coupon/', include(couponsUrls)),
    url(r'^cloud/$', GetSignedUrl.as_view())
    #url(r'^mensajes', include(apiUrls))
]

router = routers.DefaultRouter()
router.register(r'products', ProductsViewsets)
router.register(r'orders', OrderViewSet)

urlpatterns += router.urls
