from django.contrib import admin
from . models import ColourRequest

class ColourRequestAdmin(admin.ModelAdmin):
    list_display = ('source', 'user', 'colour', 'message', 'requested')
    search_fields = ('colour', 'source', 'user', 'message')

admin.site.register(ColourRequest, ColourRequestAdmin)