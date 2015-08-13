# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url,include
from rest_framework.routers import SimpleRouter
from viewsets import CategoryViewSet

from . import views

router = SimpleRouter(trailing_slash = True)
router.register(r'rest',CategoryViewSet)

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^(?P<pk>\d+)/$', views.detail, kwargs={'slug': "", }, name='detail'),
    url(r'^(?P<pk>\d+)/(?P<slug>[\w-]+)/$', views.detail, name='detail'),
    url(r'',include(router.urls)),
]
