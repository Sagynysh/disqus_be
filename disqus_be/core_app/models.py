"""This module contains DB models"""
from django.db import models
from django.utils import timezone


class Site(models.Model):
    url = models.CharField(max_length=1000)


class Comment(models.Model):
    nickname = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    comment = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=timezone.now)
    site = models.ForeignKey(Site)
