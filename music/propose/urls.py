# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from propose import views

urlpatterns = [
    url(r'^test/$', views.test),
    url(r'^track/$', views.TrackList.as_view()),
    url(r'^track/(?P<pk>[0-9a-zA-Z]+)/$',views.TrackDetail.as_view()),
    url(r'^tag/$',views.TagList.as_view()),
    url(r'^tag/(?P<pk>[\-0-9a-zA-Zㄱ-힣]+)/$',views.TagDetail.as_view()),
    url(r'^jamm/$', views.JammList.as_view()),
    url(r'^jamm/(?P<pk>[0-9a-zA-z]+)/$',views.JammDetail.as_view()),
    url(r'^play/$',views.PlayList.as_view()),
    url(r'^play/(?P<pk>[0-9]+)/$',views.PlayDetail.as_view()),
    url(r'^address/$',views.AddressList.as_view()),
    url(r'^address/(?P<pk>[\w\ 0-9ㄱ-힣]+)/$',views.AddressDetail.as_view()),
    url(r'^address/(?P<pk>[\w\ 0-9ㄱ-힣]+)/proposal/$',views.address_proposal_list),
]
