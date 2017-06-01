# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#import operator
from rest_framework import serializers
from propose.models import *
from django.db.models import Sum, Q
import operator
import random
class AddressSerializer(serializers.ModelSerializer):
    play_num = serializers.SerializerMethodField()
    def get_play_num(self,obj):
        return Play.objects.filter(address=obj.address).count()
    class Meta:
        model = Address
        fields = ('address','play_num')

class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ('id','date','track','address')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name','score')

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id','album','name','is_title')

class MTMSerializer(serializers.ModelSerializer):
    class Meta:
        model = MTM
        fields = ('id','track','tag','harmony')

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id','name')

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id','name','gender','score')

class AASerializer(serializers.ModelSerializer):
    class Meta:
        model = AA
        fields = ('id','album','artist')

class ProposalSerializer(serializers.BaseSerializer):
    def to_representation(self,obj):
        sorted_play = Play.objects.filter(address=obj.address)[:1000]
        tag = {}
        for p in sorted_play:
            mtm=MTM.objects.filter(track=p.track)[:3]
            for j in mtm:
                tag[j.tag]=tag.get(j.tag,0)-j.harmony
        track = {}
        sorted_tag=sorted(tag.items(),key=operator.itemgetter(1))[:10]
        proposal_tag=[]
        for tn in sorted_tag:
            proposal_tag.append(tn[0].name)
            mtm=MTM.objects.filter(tag=tn[0])[:3]
            for j in mtm:
                track[j.track]=track.get(j.track,0)+j.harmony*tn[1]
        sorted_track=sorted(track.items(),key=operator.itemgetter(1))[:10]
        proposal_track=[]
        proposal_artist=[]
        proposal_album=[]
        for tn in sorted_track:
            proposal_track.append([tn[0].name,tn[0].is_title,tn[0].album.name])
            sorted_artist=AA.objects.filter(album=tn[0].album)
            for an in sorted_artist:
                infor=[an.artist.name,an.artist.gender,an.artist.score]
                if infor not in proposal_artist:
                    proposal_artist.append(infor)
                    sorted_album=AA.objects.filter(artist=an.artist)[:3]
                    for aan in sorted_album:
                        if aan.album.name not in proposal_album:
                            proposal_album.append(aan.album.name)
        return [
                proposal_tag,proposal_track,
                random.sample(proposal_artist,min([5,len(proposal_artist)])),
                random.sample(proposal_album,min([5,len(proposal_album)]))
                ]
    class Meta:
        model = Address
