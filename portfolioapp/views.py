from django.shortcuts import render
from .models import photos, contact

# Create your views here.
def viewpage(request):
    photo = photos.objects.all()
    ph = {'photos': photos, 'contact': contact}
    return render(request, 'portfolioapp/index.html', ph)