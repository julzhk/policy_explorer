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

logger = logging.getLogger(__name__)


class Topic(models.Model):
    slug = models.SlugField(max_length=128)
    name = models.CharField(max_length=512)
    url = models.URLField(max_length=512)
    source = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('pk',)

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

    @classmethod
    def populate_topic(cls):
        session = HTMLSession()
        session = session.get('https://policy.greenparty.org.uk/eu.html')
        menu = session.html.find('.spchunk ul')[1]
        items = menu.find('li')
        for item in items:
            label, href = item.text, item.find('a')[0].attrs.get('href')
            topic, _ = Topic.objects.get_or_create(slug=label)
            topic.name = label
            topic.url = href
            topic.save()


class Policy(models.Model):
    slug = models.SlugField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    code = models.CharField(max_length=64, blank=True, null=True)
    topic = models.ForeignKey('Topic', on_delete=models.DO_NOTHING, blank=True, null=True)
    text = models.TextField()
    tags = TaggableManager(blank=True)
    class Meta:
        ordering = ('code',)
        verbose_name_plural = 'Policies'

    def __str__(self):
        return f'{self.code}:{self.name}'


