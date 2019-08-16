from django.shortcuts import render
from policy.models import Policy, Topic
from persona.models import Person
def homepage(request):
    return render(request, 'topic/homepage.html',
                  {
                      'persons':Person.objects.filter(published=True)}
                  )


def policy_view(request, pk=1):
    topic = Topic.objects.get(pk=int(pk))
    return render(request, 'topic/topic.html',
                  {'topic':topic}
                  )
def topics_view(request):
    topics = Topic.objects.all()
    return render(request, 'topic/topics.html',
                  {'topics':topics}
                  )

