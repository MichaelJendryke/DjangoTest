from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /user/1/
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail')
    ]