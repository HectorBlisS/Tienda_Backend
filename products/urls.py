from django.conf.urls import url
from .views import DocumentView, CategoryView, ProductListOwner, MainProductView


urlpatterns = [
    url(r'^document/(?P<doc_id>\d+)/$', DocumentView.as_view()),
    url(r'^categorias/$', CategoryView.as_view()),
    url(r'^products/$', ProductListOwner.as_view()),
    url(r'^mainProduct/$', MainProductView.as_view())
]
