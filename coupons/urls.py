from django.conf.urls import url
from .views import CouponApply

urlpatterns = [
	url(r'^apply/$', CouponApply.as_view())
]