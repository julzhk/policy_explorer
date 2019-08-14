from django.shortcuts import render
from policy.models import Policy, Topic

def homepage(request):
    return render(request, 'topic/homepage.html',
                  {}
                  )


def policy_view(request, pk=1):
    topic = Topic.objects.get(pk=int(pk))
    return render(request, 'topic/topic.html',
                  {'topic':topic}
                  )

