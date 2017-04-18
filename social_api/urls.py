
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as apiUrls
from rest_framework_social_oauth2 import urls as socialUrls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include(socialUrls)),
    url(r'^', include(apiUrls))
]
