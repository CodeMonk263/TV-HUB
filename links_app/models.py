from django.db import models

class ShowsModel(models.Model):
    title = models.CharField(max_length=60)
    href = models.CharField(max_length=300)
    thumbnail_src = models.CharField(max_length=400, default='None')

class SeasonModel(models.Model):
    title = models.CharField(max_length=60)
    season = models.CharField(max_length=3, default="0")
    href = models.CharField(max_length=500)

class EpisodesModel(models.Model):
    title = models.CharField(max_length=60)
    season = models.CharField(max_length=5, default="0")
    episode = models.CharField(max_length=3, default="0")
    href = models.CharField(max_length=400)
