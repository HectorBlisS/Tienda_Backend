from django.conf.urls import url
from .views import DocumentView, CategoryView


urlpatterns = [
    url(r'^document/(?P<doc_id>\d+)/$', DocumentView.as_view()),
    url(r'^categorias/', CategoryView.as_view())
]
