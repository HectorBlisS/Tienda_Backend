from rest_framework import routers
from .views import ListasViewset, UserData, UserEdit, UserCreateView
from django.conf.urls import url, include


router = routers.DefaultRouter()
router.register(r'mensajes', ListasViewset)
router.register(r'signup', UserCreateView)

urlpatterns = [
	url(r'^profile/$', UserData.as_view()),
	url(r'^profile/(?P<pk>\d+)/$', UserEdit.as_view()),
	url(r'^', include(router.urls))
]

# urlpatterns += [url(r'^signup/$', UserCreateView.as_view())]

#curl -X POST -d "client_id=FFmx98omsLyUpy2tBvMwImmhEc1uJ6rdau5mbD7I&client_secret=QuGWmGbeWuhG2gp1C8yAnZAOBLMtoe4cjauqBvmbVCgNpGGWllpJpV43mM6hE4O59yD72dPX8AuJ4l2Kn9Bz3pyNT3iQ0DRwlaljW3Lk1FpfYXlSjT7PBX1BazwGfDiq&grant_type=password&username=admin&password=administrador" https://erik.fixter.org/auth/token/
