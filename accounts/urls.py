from rest_framework import routers
from .views import ListasViewset
from django.conf.urls import url


router = routers.DefaultRouter()
router.register(r'mensajes', ListasViewset)

urlpatterns = router.urls