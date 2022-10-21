# Generated by Django 4.1.1 on 2022-10-13 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AlbumName', models.CharField(default='New Album', max_length=100)),
                ('AlbumCreationDate', models.DateTimeField()),
                ('AlbumReleaseTime', models.DateTimeField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('isApproved', models.BooleanField(default=False)),
                ('AlbumArtist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.artist')),
            ],
        ),
    ]
