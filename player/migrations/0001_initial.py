# Generated by Django 4.0.4 on 2022-06-03 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.FileField(blank=True, upload_to='uploads/songs', verbose_name='песни')),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.FileField(blank=True, upload_to='uploads/songs', verbose_name='песни')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'песни',
                'verbose_name_plural': 'песни',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('password', models.CharField(blank=True, max_length=50)),
                ('time_created', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профиль',
            },
        ),
    ]