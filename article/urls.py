from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /article/2016/
    url(r'^(?P<code>[0-9]+)/$', views.full, name='detail'),
]