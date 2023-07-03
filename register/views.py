from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

def home(request):
    events = Event.objects.all()
    return render(request, "register/index.html", {"events": events})

def create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = EventForm()
    
    return render(request, 'register/create.html', {'form': form})
