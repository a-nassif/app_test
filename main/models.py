from django.db import models

# Create your models here.
from django.conf import settings

from django.contrib.auth.models import User


class Project(models.Model):

    # @staticmethod
    def get_zero_user():
        return [0]

    slug = models.SlugField(null=True, blank=True, unique=True, default="")
    project_title = models.CharField(null=True, blank=True, max_length=120)
    project_post = models.TextField(null=True, blank=True)
    project_cat = models.CharField(null=True, blank=True, max_length=20)
    project_thumb = models.FileField(upload_to='upload_image_path', null=True, blank=True)
    project_movie = models.FileField(upload_to='upload_image_path', null=True, blank=True, default='False')
    project_views = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='project_views',
                                           default=get_zero_user()
                                           )
    project_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='project_likes',
                                           default=get_zero_user()
                                           )
    project_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)




