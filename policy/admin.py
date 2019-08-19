# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Topic, Policy

class PolicyInline(admin.TabularInline):
    model = Policy
    fields = ['code', 'name','text']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url',)
    search_fields = ('name',)
    inlines = [PolicyInline, ]
    prepopulated_fields = {'slug': ['name']}


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'topic', 'tag_list', )
    list_filter = ('topic', )
    raw_id_fields = ('tags',)
    search_fields = ('name','text')
    prepopulated_fields = {'slug': ['name']}

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    def get_queryset(self, request):
        return super(PolicyAdmin, self).get_queryset(request).prefetch_related('tags')
