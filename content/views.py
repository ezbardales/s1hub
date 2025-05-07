from django.shortcuts import render, redirect, get_object_or_404
from .models import Cadet
from .forms import CadetForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def home(request):
    # retrieve all challenges
    cadets = Cadet.objects.all()
    # render the page with the information about the challenges
    return render(request, 'content/home.html', {'cadets': cadets})

@user_passes_test(lambda u: u.is_superuser)
def add_cadet(request):
    # upon submission, retrieve and save the form data if it is valid. Then redirect to the home page.
    if request.method == 'POST':
        form = CadetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    # otherwise, initialize the form and render the page to allow data entry
    else:
        form = CadetForm()
    return render(request, 'content/add_cadet.html', {'form': form})

def cadet_detail(request, cadet_id):
    cadet = get_object_or_404(Cadet, pk=cadet_id)   

    return render(request, 'content/cadet_detail.html', {'cadet': cadet})

def show_shifts(request):
    return render(request, 'content/shifts.html')