# tunr/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('songs/', views.song_list, name='song_list'),
    path('artists/<int:pk>', views.artist_detail, name='artist_detail'),
    path('songs/<int:pk>', views.song_detail, name='song_detail'),
    path('artists/new', views.artist_create, name='artist_create'),
    path('songs/new', views.song_create, name='song_create'),
    path('artists/<int:pk>/edit', views.artist_edit, name='artist_edit'),
    path('artists/<int:pk>/delete', views.artist_delete, name='artist_delete'),
    path('songs/<int:pk>/delete', views.song_delete, name='song_delete'),
]