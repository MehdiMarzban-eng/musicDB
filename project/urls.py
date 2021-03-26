"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from musicDB import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^artists/',views.ArtistList.as_view()),
    url(r'^song/', views.SongList.as_view()),
    url(r'^album/', views.AlbumList.as_view()),
    url(r'^label/', views.LabelList.as_view()),
    url(r'^genre/', views.GenreList.as_view()),
    url(r'^playlist/', views.PlaylistList.as_view()),
    url(r'^podcast/', views.PodcastList.as_view()),
    url(r'^producer/', views.ProducerList.as_view()),

]
