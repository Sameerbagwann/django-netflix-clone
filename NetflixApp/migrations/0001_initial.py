# Generated by Django 5.0.6 on 2024-06-06 08:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uu_id', models.UUIDField(default=uuid.uuid4)),
                ('title', models.CharField(max_length=255)),
                ('desciption', models.TextField()),
                ('releasedate', models.DateField()),
                ('genre', models.CharField(choices=[('action', 'Action'), ('comedy', 'Comedy'), ('drama', 'Drama'), ('horror', 'Horror'), ('romantic', 'Romantic'), ('fantacy', 'Fantacy')], max_length=100)),
                ('length', models.PositiveIntegerField()),
                ('image_card', models.ImageField(upload_to='movie_images/')),
                ('image_cover', models.ImageField(upload_to='movie_images/')),
                ('video', models.FileField(upload_to='movie_videos/')),
                ('movie', models.IntegerField(default=0)),
            ],
        ),
    ]
