import logging
from django.db import models
from requests_html import HTMLSession

import datetime
from django.conf import settings
from django.db.models import Count, Sum
from django.forms.models import model_to_dict
from django.urls import reverse
from taggit.managers import TaggableManager
import requests

logger = logging.getLogger(__name__)


class Topic(models.Model):
    slug = models.SlugField(max_length=128)
    name = models.CharField(max_length=512)
    url = models.URLField(max_length=512)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def populate_policies(self):
        session = HTMLSession()
        session = session.get(self.url)
        self.source = session.html.html
        self.save()
        main_section = session.html.find('.gu2', first=True)
        paras = main_section.find('p')
        policies = {p.find('a')[0].attrs.get('name'): p.text for p in paras if p.find('a')}
        for key in policies:
            data = policies.get(key)
            policy, _ = Policy.objects.get_or_create(slug=key)
            policy.name = key
            policy.code = key
            policy.topic = self
            policy.text = data
            policy.save()


class Policy(models.Model):
    slug = models.SlugField(max_length=128)
    name = models.CharField(max_length=512)
    code = models.CharField(max_length=64)
    topic = models.ForeignKey('Topic', on_delete=models.DO_NOTHING)
    text = models.TextField()
    tags = TaggableManager(blank=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    tags_reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.code}:{self.name}'

    class Meta:
        verbose_name_plural = 'Policies'

