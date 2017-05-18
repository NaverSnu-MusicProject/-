# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#import operator
from rest_framework import serializers
from propose.models import *
from django.db.models import Sum, Q

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('track_id','track_title','is_title')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag_name','tag_score')

class MTMSerializer(serializers.ModelSerializer):
    class Meta:
        model = MTM
        fields = ('mtm_id','mtm_date','track','tag','harmony')

class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ('id','play_date','track_id','address')

class AddressSerializer(serializers.ModelSerializer):
    play_num = serializers.SerializerMethodField()
    def get_play_num(self,obj):
        return Play.objects.filter(address=obj.address).count()
    class Meta:
        model = Address
        fields = ('address','play_num')

class ProposalSerializer(serializers.BaseSerializer):
    def to_representation(self,obj):
        play = Play.objects.filter(address=obj.address)
        tag = {}
        for p in play:
            mtm=MTM.objects.filter(track=p.track_id)
            for j in mtm:
                tag[j.tag]=tag.get(j.tag,0)+j.harmony # *Tag.get(pk=j.tag_name).tag_score
            # mean
        track = {}
        for tn in tag:
            mtm=MTM.objects.filter(tag=tn)
            for j in mtm:
                track[Track.objects.get(pk=j.track_id).track_title] = track.get(j.track_id,0)+j.harmony*tag[tn]
        return track
    class Meta:
        model = Address
