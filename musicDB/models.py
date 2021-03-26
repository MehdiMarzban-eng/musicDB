from django.db import models


# '''
class Genre(models.Model):
    genreName = models.CharField(max_length=30)

    def __str__(self):
        return self.genreName


class Label(models.Model):
    labelID = models.IntegerField(primary_key=True, default=0)
    labelName = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    founder = models.CharField(max_length=30)

    def __str__(self):
        return self.labelName


# '''
class Artist(models.Model):
    artistID = models.IntegerField(primary_key=True, default=1)
    artistName = models.CharField(max_length=30 )
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    RecordLabel = models.ForeignKey(Label,on_delete=models.CASCADE)

    def __str__(self):
        return self.artistName


# '''

class Album(models.Model):
    albumID = models.IntegerField(primary_key=True, default=0)
    albumName = models.CharField(max_length=30)
    releaseDate = models.DateField()
    artist = models.ManyToManyField(Artist)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.albumName


class Song(models.Model):
    songName = models.CharField(max_length=30)
    releaseDate = models.DateField()
    # the song duration is in seconds
    duration = models.IntegerField(default=0)
    key = models.CharField(max_length=2, default='C')
    bpm = models.SmallIntegerField(default=0)
    explicit = models.BooleanField(default=False)
    songID = models.IntegerField(primary_key=True)
    artist = models.ManyToManyField(Artist)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.songName


class Playlist(models.Model):
    playlistID = models.IntegerField(default=0)
    playlistName = models.CharField(max_length=999)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.playlistName
# '''
class Producer(models.Model):
    producerID = models.IntegerField(primary_key=True,default=1)
    producerName = models.CharField(max_length=30)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.producerName

class Podcast(models.Model):
    podcastID = models.IntegerField(primary_key=True, default=1)
    podcastName = models.CharField(max_length=30)
    genre = models.ManyToManyField(Genre)
    duration = models.IntegerField(default=0)
    releaseDate = models.DateField()
    explicit = models.BooleanField(default=False)

    def __str__(self):
        return self.podcastName
