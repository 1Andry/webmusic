# Generated by Django 4.0.5 on 2022-06-27 18:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='is_favorite',
        ),
        migrations.AddField(
            model_name='album',
            name='is_favorite',
            field=models.ManyToManyField(blank=True, related_name='fav_videos', to=settings.AUTH_USER_MODEL),
        ),
    ]
