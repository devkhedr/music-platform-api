from datetime import datetime
from email.policy import default
from datetime import datetime
from django.db import models
from artists.models import Artist
from model_utils.fields import AutoCreatedField
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from imagekit.models import ProcessedImageField


class TimeStampedModel(models.Model):
    created_at = AutoCreatedField(_('created_at'), null=False)

    class Meta:
        abstract = True


class Album(TimeStampedModel):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="New Album")
    release_date = models.DateTimeField(blank=False, null=False)
    cost = models.DecimalField(
        max_digits=6, decimal_places=2, blank=False, null=False)
    is_approved = models.BooleanField(default=False, blank=False)

    def songs_count(self):
        return self.song_set.count()

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=100, blank=True, null=False)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=False)
    thumb = ProcessedImageField(upload_to='thumbs/', format='JPEG')
    audio = models.FileField(
        upload_to='audios/', validators=[FileExtensionValidator(['mp3', 'wav'])])

    def __str__(self):
        return self.name
