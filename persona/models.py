import logging
from django.db import models
from requests_html import HTMLSession
from requests_html import HTMLSession

import datetime
from django.conf import settings
from django.db.models import Count, Sum
from django.forms.models import model_to_dict
from django.urls import reverse
from taggit.managers import TaggableManager
import requests
from django.conf import settings
from taggit.managers import TaggableManager

logger = logging.getLogger(__name__)


class Person(models.Model):
    name = models.CharField(max_length=512)
    image = models.ImageField(upload_to=f'{settings.CLOUDCUBE_URL}/public', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    published = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)

    def get_absolute_url(self):
        return reverse('person ' , args=(self.pk,))


    def __str__(self):
        return f'{self.name}'
