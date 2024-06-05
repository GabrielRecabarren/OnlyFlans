from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Flan, ContactForm, Review
from .forms import ContactFormModelForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

# Create your views here.

def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    
    context = {
        'flanes_publicos': flanes_publicos,
    }
    
    return render(request, 'index.html', context)

def acerca(request):
    return render(request, 'about.html', {})


@login_required
def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'flanes_privados': flanes_privados,
    }

    return render(request, 'welcome.html', context)

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormModelForm()

    return render(request, 'contact.html', {'form': form})

def exito(request):
    return render(request, 'success.html', {})

@login_required
def add_review(request, flan_uuid):
    flan = get_object_or_404(Flan, flan_uuid=flan_uuid)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.flan = flan
            review.save()
            return redirect('flan_detail', flan_uuid=flan.flan_uuid)
    else:
        form = ReviewForm(initial={'flan': flan})
    return render(request, 'add_review.html', {'form': form, 'flan': flan})

def flan_detail(request, flan_uuid):
    flan = get_object_or_404(Flan, flan_uuid=flan_uuid)
    reviews = Review.objects.filter(flan=flan)
    stars = range(5)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'flan_detail.html', {'flan': flan, 'reviews': reviews, 'average_rating':average_rating, 'stars':stars})
