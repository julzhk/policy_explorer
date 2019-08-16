"""policyExplorer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from taggit_templatetags2 import urls as taggit_templatetags2_urls

from policy.views import policy_view,topics_view,  homepage
from persona.views import person_view

urlpatterns = [
    path('topic/', policy_view, name='topic'),
    path('topic/<pk>/', policy_view ),
    path('topics/', topics_view, name='topics' ),
    path('person/<pk>/', person_view , name='person'),

    url(r'^tags/', include('taggit_templatetags2.urls')),

    path('django-admin/', admin.site.urls),
    path('', homepage, name='home'),

]
