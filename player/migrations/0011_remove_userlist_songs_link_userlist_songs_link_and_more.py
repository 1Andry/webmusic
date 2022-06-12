# Generated by Django 4.0.4 on 2022-06-12 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('player', '0010_alter_songs_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlist',
            name='songs_link',
        ),
        migrations.AddField(
            model_name='userlist',
            name='songs_link',
            field=models.ManyToManyField(blank=True, null=True, to='player.songs', verbose_name='songs_link'),
        ),
        migrations.AlterField(
            model_name='userlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]