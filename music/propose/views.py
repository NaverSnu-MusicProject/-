# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from propose.models import *
from propose.serializers import *
from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class TrackList(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class TrackDetail(generics.RetrieveAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetail(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class MMFList(generics.ListCreateAPIView):
    queryset = MMF.objects.all()
    serializer_class = MMFSerializer

class MMFDetail(generics.RetrieveAPIView):
    queryset = MMF.objects.all()
    serializer_class = MMFSerializer

class PlayList(generics.ListCreateAPIView):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer

class PlayDetail(generics.RetrieveAPIView):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
#    def perform_create(self, serializer):
#        serializer.save(owner=self.request.user)

class AddressDetail(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

@api_view(['GET'])
def address_proposal_list(request, pk):
    try:
        address = Address.objects.get(pk = pk)
    except Address.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProposalSerializer(address)
        return Response(serializer.data)

def test(request):
    return render(request, 'propose/test.html',{})

def xx(request):
    return render(request, 'propose/xx.html',{})
