from django.conf.urls import url
from .views import DocumentView


urlpatterns = [
    url(r'^document/(?P<doc_id>\d+)/$', DocumentView.as_view())
]
