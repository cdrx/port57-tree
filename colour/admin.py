from django.contrib import admin
from . models import Colour

class ColourAdmin(admin.ModelAdmin):
    list_display = ('name', 'r', 'g', 'b')
    search_fields = ('name', )

admin.site.register(Colour, ColourAdmin)

