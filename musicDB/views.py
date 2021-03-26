from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Artist

#'''
from .models import Song
from .models import Label
from .models import Genre
from .models import Album
from .models import Playlist
from .models import Producer
from .models import Podcast

#'''
from .serializers import ArtistSerializer

#'''
from .serializers import SongSerializer
from .serializers import AlbumSerializer
from .serializers import LabelSerializer
from .serializers import GenreSerializer
from .serializers import PlaylistSerializer
from .serializers import PodcastSerializer
from .serializers import ProducerSerializer
#'''


class ArtistList(APIView):
    def get(self, request):
        artist1 = Artist.objects.all()
        serializer = ArtistSerializer(artist1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


#'''
class SongList(APIView):
    def get(self, request):
        song1 = Song.objects.all()
        serializer = SongSerializer(song1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class AlbumList(APIView):
    def get(self, request):
        album1 = Album.objects.all()
        serializer = AlbumSerializer(album1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class LabelList(APIView):
    def get(self, request):
        Label1 = Label.objects.all()
        serializer = LabelSerializer(Label1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class GenreList(APIView):
    def get(self, request):
        genre1 = Genre.objects.all()
        serializer = GenreSerializer(genre1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class PlaylistList(APIView):
    def get(self, request):
        playlist1 = Playlist.objects.all()
        serializer = PlaylistSerializer(playlist1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class PodcastList(APIView):
    def get(self, request):
        podcast1 = Podcast.objects.all()
        serializer = PodcastSerializer(podcast1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class ProducerList(APIView):
    def get(self, request):
        producer1 = Producer.objects.all()
        serializer = PlaylistSerializer(producer1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

#'''
