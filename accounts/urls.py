from rest_framework import routers
from .views import ListasViewset, UserCreateView
from django.conf.urls import url


router = routers.DefaultRouter()
router.register(r'mensajes', ListasViewset)
router.register(r'signup', UserCreateView)

urlpatterns = router.urls

# urlpatterns += [url(r'^signup/$', UserCreateView.as_view())]

#curl -X POST -d "client_id=FFmx98omsLyUpy2tBvMwImmhEc1uJ6rdau5mbD7I&client_secret=QuGWmGbeWuhG2gp1C8yAnZAOBLMtoe4cjauqBvmbVCgNpGGWllpJpV43mM6hE4O59yD72dPX8AuJ4l2Kn9Bz3pyNT3iQ0DRwlaljW3Lk1FpfYXlSjT7PBX1BazwGfDiq&grant_type=password&username=admin&password=administrador" https://erik.fixter.org/auth/token/
