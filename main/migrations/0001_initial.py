# Generated by Django 3.0.3 on 2020-02-08 14:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='', null=True, unique=True)),
                ('project_title', models.CharField(blank=True, max_length=120, null=True)),
                ('project_post', models.TextField(blank=True, null=True)),
                ('project_cat', models.CharField(blank=True, max_length=20, null=True)),
                ('project_thumb', models.FileField(blank=True, null=True, upload_to='upload_image_path')),
                ('project_movie', models.FileField(blank=True, default='False', null=True, upload_to='upload_image_path')),
                ('project_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('project_likes', models.ManyToManyField(blank=True, default=0, related_name='project_likes', to=settings.AUTH_USER_MODEL)),
                ('project_views', models.ManyToManyField(blank=True, default=0, related_name='project_views', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]