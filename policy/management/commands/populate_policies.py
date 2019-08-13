import logging
import random
from policy.models import Topic
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):


    def handle(self, *args, **options):
        logger.info("CALLED: populate policies")
        for topic in Topic.objects.all():
            topic.populate_policies()
        self.stdout.write(self.style.SUCCESS('Successfully complete'))

