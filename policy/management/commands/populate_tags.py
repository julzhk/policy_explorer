import logging
import random
from policy.models import Policy
from django.core.management.base import BaseCommand
from django.conf import settings
logger = logging.getLogger(__name__)
import textrazor



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('start_id', nargs='+', type=int)
        parser.add_argument('end_id', nargs='+', type=int)

    def handle(self, *args, **options):
        start_id, end_id = 0, Policy.objects.count()
        if options['start_id']:
            print(options['start_id'])
            start_id = options['start_id'][0]
        else:
            start_id = 0
        if options['end_id']:
            end_id = options['end_id'][0]
        else:
            end_id = Policy.objects.count()
        logger.info("CALLED: populate tags")
        textrazor.api_key = settings.TEXTRAZOR_KEY
        client = textrazor.TextRazor(extractors=["topics"])
        for policy in Policy.objects.all()[start_id:end_id]:
            response = client.analyze(policy.text)
            for topic in response.topics():
                print(topic.label, topic.score)
            labels = [topic.label for topic in response.topics() if topic.score>0.25]
            policy.tags.add(*labels)
        self.stdout.write(self.style.SUCCESS('Successfully complete'))

