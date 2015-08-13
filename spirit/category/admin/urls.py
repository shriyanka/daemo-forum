# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url,include
from rest_framework.routers import SimpleRouter
from viewsets import CategoryViewSet
from . import views

router = SimpleRouter(trailing_slash = True)
router.register(r'rest',CategoryViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^update/(?P<category_id>\d+)/$', views.update, name='update'),
    url(r'',include(router.urls)),
]
