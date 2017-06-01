# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Address(models.Model):
    address = models.CharField(max_length=40,primary_key=True)
    play_num = models.PositiveIntegerField(default=0)

class Play(models.Model):
    date = models.DateTimeField()
    track = models.ForeignKey('Track',on_delete=models.CASCADE)
    address = models.ForeignKey('Address',on_delete=models.CASCADE)

class Tag(models.Model):
    id = models.PositiveIntegerField(primary_key = True)
    name = models.CharField(max_length=40)
    score = models.PositiveSmallIntegerField()
    class Meta:
        ordering = ['-score']

class Track(models.Model):
    id = models.CharField(max_length=40,primary_key = True)
    album = models.ForeignKey('Album',on_delete=models.CASCADE)
    name = models.CharField(max_length=22)
    is_title = models.BooleanField()

class MTM(models.Model):
    track = models.ForeignKey('Track',on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag',on_delete=models.CASCADE)
    harmony = models.PositiveSmallIntegerField()
    class Meta:
        ordering = ['-harmony']

class Album(models.Model):
    id = models.CharField(max_length=40,primary_key = True)
    name = models.CharField(max_length=22)

class Artist(models.Model):
    id = models.CharField(max_length=40,primary_key = True)
    name = models.CharField(max_length=12)
    gender = models.BooleanField()
    score = models.PositiveIntegerField()

class AA(models.Model):
    album = models.ForeignKey('Album',on_delete=models.CASCADE)
    artist = models.ForeignKey('Artist',on_delete=models.CASCADE)
