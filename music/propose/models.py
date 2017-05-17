# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
'''
class Album(models.Model):
    # 3D9F9389F,써든리(Suddenly),가요 > 댄스, 2014-07-18,
    # http://musicmeta.phinf.naver.net/album/001/962/1962881.jpg?type=r204Fll&v=20170405141010
    album_id = models.CharField(max_length=22,primary_key = True)
    album_title = models.CharField(max_length=22)
    genre_style = models.CharField(max_length=22)
    release_date = models.CharField(max_length=22)
    album_url = models.CharField(max_length=111)

class Artist(models.Model):
    # 3F89D98,Cold Rush, 그룹, 남성,에스토니아,
    # http://musicmeta.phinf.naver.net/artist/000/035/35551.jpg?type=r240&v=20170404122309

    artist_id = models.CharField(max_length=22,primary_key = True)
    artist_name = models.CharFied(max_length=22)
    artist_type = models.CharFied(max_length=22)
    artist_gender = models.CharFied(max_length=22)
    artist_contry = models.CharFied(max_length=22)
    artist_url = models.CharFied(max_length=101)
'''

class Track(models.Model):
    # ASD89F89, *9SDA89A,* A909FA8, 거꾸로 강을 거슬러 오르는 저 힘찬 연어들처럼, Y

    track_id = models.CharField(max_length=22,primary_key = True)
    '''
    artist_id_list??
    (1. 대표 아티스트)
    (2. 같은 트랙을 여러개 -> 가중치 문제가 생김 가중치를 둬야함 아티스트 넘버)
    artist_num =
    album_id = models.CharFied(max_length=22)
    '''
    track_title = models.CharField(max_length=22)
    is_title = models.BooleanField()

class Tag(models.Model):
    # ASD89F89,이주의발견-해외-2010-6월4주,33,20150901,2214909
    tag_name = models.CharField(max_length=22,primary_key = True)
    tag_score = models.PositiveSmallIntegerField()
    class Meta:
        ordering = ['-tag_score']

class MMF(models.Model):
    mmf_id = models.CharField(max_length=22,primary_key =True)
    mmf_date = models.DateTimeField()
    track = models.ForeignKey('Track',on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag',on_delete=models.CASCADE)
    harmony = models.PositiveSmallIntegerField()
    class Meta:
        ordering = ['-harmony']

class Address(models.Model):
    address = models.CharField(max_length=101,primary_key=True)
    play_num = models.PositiveIntegerField(default=0)
#    proposal_track = models.ForeignKey('Track',on_delete=models.CASCADE)
    class Meta:
        ordering = ['address','play_num']

class Play(models.Model):
    # 20170330045006, *IPHONE, ASD89F89, 위도, 경도
    play_date = models.DateTimeField()
    track_id = models.ForeignKey('Track',on_delete=models.CASCADE)
    address = models.ForeignKey('Address',on_delete=models.CASCADE)
    class Meta:
        ordering = ['-play_date']
