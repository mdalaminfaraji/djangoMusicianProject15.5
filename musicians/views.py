# musicians/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm

def musicians_table(request):
    combined_data = []
    musicians = Musician.objects.all()

    for musician in musicians:
        albums = Album.objects.filter(musician=musician)
        for album in albums:
            combined_data.append({
                'id': musician.id,
                'musician_name': str(musician),
                'email': musician.email,
                'album_rating': album.rating,
                'instrument_type': musician.instrument_type,
                'album_name': album.album_name,
                'release_date': album.release_date,
            })
    return render(request, 'musicians_table.html', {'combined_data': combined_data})
    
def edit_musician(request, musician_id):
    musician = get_object_or_404(Musician, pk=musician_id)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('musicians_table')
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'edit_musician.html', {'form': form, 'musician': musician})

def edit_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('musicians_table')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'edit_album.html', {'form': form, 'album': album})

