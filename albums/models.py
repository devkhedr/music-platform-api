from datetime import datetime
from email.policy import default
from unicodedata import numeric
from django.db import models
from artists.models import artist


class album(models.Model):
    album_artist = models.ForeignKey(artist, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100, default="New Album")
    album_creation_date = models.DateTimeField()
    album_release_time = models.DateTimeField(blank=False, null=False)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=False, null=False)
    is_approved = models.BooleanField(
        default=False, blank=False, help_text="Approve the album if its name is not explicit")

    def __str__(self):
        return self.album_name
