import logging
import random
from policy.models import Policy
from django.core.management.base import BaseCommand
from django.conf import settings
logger = logging.getLogger(__name__)
import textrazor



class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.info("CALLED: populate tags")
        textrazor.api_key = settings.TEXTRAZOR_KEY
        client = textrazor.TextRazor(extractors=["topics"])
        for policy in Policy.objects.all()[50:]:
            response = client.analyze(policy.text)
            for topic in response.topics():
                print(topic.label, topic.score)
            labels = [topic.label for topic in response.topics() if topic.score>0.25]
            policy.tags.add(*labels)
        self.stdout.write(self.style.SUCCESS('Successfully complete'))

