from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models import Count, Model
from users.models import CustomUser

class Artist(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, related_name = 'artist')
    stage_name = models.CharField(
        max_length=100, unique=True, blank=False, null=False)
    social_link = models.URLField(max_length=200, blank=True, null=False)

    class Meta:
        ordering = ['stage_name']

    def approved_albums(self):
        return self.album_set.filter(is_approved=True).count()

    def __str__(self):
        return self.stage_name