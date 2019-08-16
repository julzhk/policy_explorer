from django.contrib import admin

from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bio', 'published', 'tag_list')
    list_filter = ('published',)
    raw_id_fields = ('tags',)
    search_fields = ('name',)

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
