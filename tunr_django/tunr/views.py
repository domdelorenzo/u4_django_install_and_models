from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import Artist, Song
from .forms import ArtistForm

def artist_list(request):
  artists = Artist.objects.all()
  return render(request, 'tunr/artist_list.html', {'artists': artists})

def song_list(request):
  songs = Song.objects.all()
  return render(request, 'tunr/song_list.html', {'songs': songs})


def artist_detail(request, pk):
  artist=Artist.objects.get(id=pk)
  return render(request, 'tunr/artist_detail.html', {'artist':artist})

def song_detail(request, pk):
  song=Song.objects.get(id=pk)
  return render(request, 'tunr/song_detail.html', {'song':song})



from .forms import ArtistForm, SongForm

def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm()
    return render(request, 'tunr/artist_form.html', {'form': form})

def song_create(request):
  if request.method == 'POST':
    form = SongForm(request.POST)
    if form.is_valid():
      song = form.save()
      return redirect('song_detail', pk=song.pk)
  else:
    form = SongForm()
  return render(request, 'tunr/song_form.html', {'form': form})

def artist_edit(request, pk):
    artist = Artist.objects.get(pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'tunr/artist_form.html', {'form': form})