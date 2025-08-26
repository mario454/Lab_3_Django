from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Track

# Create your views here.

def alltracks(request):
    context={}
    context['tracks'] = Track.getalltracks_N_numtr()
    return render(request, 'track/list.html', context)

def Insert(request):
    if request.method == 'POST':
        Track.objects.create(name=request.POST['track'])
        return redirect('alltracks')
    return render(request, 'track/insert.html')

def Update(request, id):
    track = Track.gettrackbyid(id)
    context = {'track':track} #Get current track

    # Check updates
    if request.method == 'POST':
        track.name = request.POST['track']
        track.save()
        return redirect('alltracks') 

    return render(request, 'track/update.html', context)

def Delete(request, id):
    Track.objects.filter(id=id).delete()
    return redirect('alltracks')

