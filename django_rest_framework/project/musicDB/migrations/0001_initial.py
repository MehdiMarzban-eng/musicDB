# Generated by Django 3.1.7 on 2021-03-20 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('albumID', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('albumName', models.CharField(max_length=30)),
                ('releaseDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artistID', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('artistName', models.CharField(default='', max_length=30)),
                ('firstName', models.CharField(default='', max_length=30)),
                ('lastName', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genreName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='label',
            fields=[
                ('labelID', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('labelName', models.CharField(default='', max_length=30)),
                ('location', models.CharField(default='', max_length=30)),
                ('founder', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('songName', models.CharField(max_length=30)),
                ('releaseDate', models.DateField()),
                ('duration', models.IntegerField(default=0)),
                ('key', models.CharField(default='C', max_length=2)),
                ('bpm', models.SmallIntegerField(default=0)),
                ('explicit', models.BooleanField(default=False)),
                ('songID', models.IntegerField(primary_key=True, serialize=False)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicDB.album')),
                ('artist', models.ManyToManyField(to='musicDB.Artist')),
                ('genre', models.ManyToManyField(to='musicDB.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlistID', models.IntegerField(default=0)),
                ('playlistName', models.CharField(max_length=999)),
                ('songs', models.ManyToManyField(to='musicDB.Song')),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicDB.label'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ManyToManyField(to='musicDB.Artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ManyToManyField(to='musicDB.Genre'),
        ),
    ]
