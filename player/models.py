from django.contrib.auth.models import Permission, User
from django.db import models


class Album(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=500)
    album_logo = models.ImageField(default='nones.png')
    is_favorite = models.ManyToManyField(User, related_name="fav_s", blank=True)

    def __str__(self):
        return self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    audio_file = models.FileField(default='')
    is_favorite = models.ManyToManyField(User, related_name="fav_song", blank=True)

    def __str__(self):
        return str(self.audio_file)
