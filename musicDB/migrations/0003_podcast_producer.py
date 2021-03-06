# Generated by Django 3.1.7 on 2021-03-23 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicDB', '0002_auto_20210320_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('producerID', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('producerName', models.CharField(max_length=30)),
                ('songs', models.ManyToManyField(to='musicDB.Song')),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('podcastID', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('podcastName', models.CharField(max_length=30)),
                ('duration', models.IntegerField(default=0)),
                ('releaseDate', models.DateField()),
                ('explicit', models.BooleanField(default=False)),
                ('genre', models.ManyToManyField(to='musicDB.Genre')),
            ],
        ),
    ]
