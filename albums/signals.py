from django.db.models.signals import pre_save, pre_delete, post_delete, post_save
from django.dispatch import receiver
from .models import Album, Song
from .tasks import send_email_for_new_album


@receiver(pre_save, sender=Song)
def song_pre_save(sender, instance, **kwargs):
    if instance.name == None or instance.name == '':
        instance.name = instance.album.name


@receiver(post_save, sender=Album)
def album_post_save(sender, instance, created, *args, **kwargs):
    if created:
        send_email_for_new_album(instance.name, instance.artist.id)


@receiver(pre_delete, sender=Song)
def song_delete(sender, instance, **kwargs):
    flag = 0

    @receiver(pre_delete, sender=Album)
    def album_delete_check(**kwargs2):
        nonlocal flag
        flag = 1

    @receiver(post_delete, sender=Song)
    def song_delete_check(**kwargs3):
        nonlocal flag
        if flag == 0 and kwargs3['instance'].album.song_set.count() < 1:
            instance.save()
