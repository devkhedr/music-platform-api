from celery import shared_task
from django.core.mail import send_mail
from celery import shared_task
from time import sleep
from artists.models import Artist
from django.utils import timezone


@shared_task()
def send_email_for_new_album(name, artist_id):
    artist = Artist.objects.get(id=artist_id)
    sleep(1)
    send_mail(
        f'Congratulations !',
        f'Congratulations {artist.stage_name} on your new album {name}. 🎉',
        'Music Paltform',
        [artist.user.email],
        fail_silently=False,
    )
    return None


@shared_task()
def send_mail_every_day_task():
    for artist in Artist.objects.all():
        last_album = artist.albums.all().order_by('created_at').first()
        if last_album.created.date() < timezone.now() - timezone.timedelta(days=30):
            message = 'Hi ' + artist.stage_name + \
                ", You haven't created an album in the past 30 days.\nSo, we want to let you know that your inactivity is causing your popularity on our platform to decrease."
            send_mail('Warning !', message,
                      'Music Platform', [artist.user.email])
