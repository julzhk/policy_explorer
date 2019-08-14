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

logger = logging.getLogger(__name__)


class Person(models.Model):
    name = models.CharField(max_length=512)
    image = models.ImageField(upload_to=settings.CLOUDCUBE_URL, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
