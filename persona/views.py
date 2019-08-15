from django.shortcuts import render
from persona.models import Person
from policy.models import Policy
def person_view(request, pk):
    this_person = Person.objects.get(pk=int(pk))
    tags = this_person.tags.names()
    policies = Policy.objects.filter(tags__name__in=tags).distinct()
    return render(request, 'persona/personpage.html',
                  {
                      'person': this_person,
                      'policies':policies
                  },
                  )