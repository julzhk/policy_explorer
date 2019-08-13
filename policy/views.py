from django.shortcuts import render
from policy.models import Policy, Topic

def policy_view(request, topic_slug=None):
    topic = Topic.objects.get(slug=topic_slug)
    return render(request, 'topic/topic.html',
                  {'topic':topic}
                  )
