from django.contrib import admin
from . models import Artist
#'''
from . models import Song
from . models import Genre
from . models import Album
from . models import Label
from . models import Playlist
from . models import Podcast
from . models import Producer
#'''
# Register your models here.

admin.site.register(Artist)
#'''
admin.site.register(Song)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Label)
admin.site.register(Playlist)
admin.site.register(Podcast)
admin.site.register(Producer)

#'''