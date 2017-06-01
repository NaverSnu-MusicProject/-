# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from propose import views
urlpatterns = [
    url(r'^test/$', views.test),
    url(r'^xx/$',views.xx),
    url(r'^track/$', views.TrackList.as_view()),
    url(r'^track/(?P<pk>[0-9A-Z]+)/$',views.TrackDetail.as_view()),
    url(r'^tag/$',views.TagList.as_view()),
    url(r'^tag/(?P<pk>[0-9]+)/$',views.TagDetail.as_view()),
    url(r'^mtm/$', views.MTMList.as_view()),
    url(r'^mtm/(?P<pk>[0-9]+)/$',views.MTMDetail.as_view()),
    url(r'^play/$',views.PlayList.as_view()),
    url(r'^play/(?P<pk>[0-9]+)/$',views.PlayDetail.as_view()),
    url(r'^album/$',views.AlbumList.as_view()),
    url(r'^album/(?P<pk>[0-9A-Z]+)/$',views.AlbumDetail.as_view()),
    url(r'^artist/$',views.ArtistList.as_view()),
    url(r'^artist/(?P<pk>[0-9A-Z]+)/$',views.ArtistDetail.as_view()),
    url(r'^aa/$',views.AAList.as_view()),
    url(r'^aa/(?P<pk>[0-9]+)/$',views.AADetail.as_view()),
    url(r'^address/$',views.AddressList.as_view()),
    url(r'^address/(?P<pk>[0-9ㄱ-힣]+)/$',views.AddressDetail.as_view()),
    url(r'^address/(?P<pk>[0-9ㄱ-힣]+)/proposal/$',views.address_proposal_list),
]
