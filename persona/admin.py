from django.contrib import admin

from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bio', 'published')
    list_filter = ('published',)
    raw_id_fields = ('tags',)
    search_fields = ('name',)
