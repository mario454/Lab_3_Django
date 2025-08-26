from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Trainee
from track.models import Track

# Create your views here.

def Alltrainee(request):
    context={}
    context['trainees'] = Trainee.getalltrainees().order_by('id')
    return render(request, 'trainee/list.html', context)

def Insert(request):
    if request.method == 'POST':
        Trainee.objects.create(name=request.POST['trName'],
                               email=request.POST['trEmail'], 
                               image=request.FILES.get('trImage'),
                               trackid=Track.gettrackbyid(request.POST['trtrack']))
        return redirect('alltrainees')
    
    context = {}
    context['tracks'] = Track.getalltracks()
    return render(request, 'trainee/insert.html', context)

def Update(request, id):
    trainee = Trainee.gettraineebyid(id)
    context = {'trainee':trainee}
    context['tracks'] = Track.getalltracks()

    if request.method == 'POST':
        trainee.name = request.POST['trName']
        trainee.email = request.POST['trEmail']
        trainee.trackid = Track.gettrackbyid(request.POST['trtrack']) # Get Object
        if request.FILES.get('trImage'):
            trainee.image = request.FILES['trImage']
        
        if request.POST.get('trstatus'):
            trainee.status = True
        else:
            trainee.status = False

        
        
        trainee.save()
        return redirect('alltrainees')
    
    return render(request, 'trainee/update.html', context)

def Delete(request, id):
    Trainee.objects.filter(id=id).update(status=False)
    return redirect('alltrainees')
