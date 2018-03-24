from django.conf.urls import url
from . import views



app_name = 'sentiment_api'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'twitter/$', views.twitter, name='twitter'),
]
