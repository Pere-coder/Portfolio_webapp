from django.shortcuts import render
from .models import photos, contact


# Create your views here.
def viewpage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        new_message = contact(name=name, email=email, message=message)
        new_message.save()
    return render(request, 'portfolioapp/index.html')