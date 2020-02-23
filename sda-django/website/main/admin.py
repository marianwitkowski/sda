from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Movie)
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    #fields = ["title", "imdb"]
    list_display = ('title', 'year', 'imdb')
    list_filter = ("year", "released")
    search_fields = ('title', 'description')

admin.site.register(Actor)