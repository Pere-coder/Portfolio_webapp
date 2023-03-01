from django.shortcuts import render
from .models import photos, contact
from django.contrib import messages

# Create your views here.
def viewpage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
       
        new_message = contact(name=name, email=email, message=message)
        messages.success(request, f'Dear {name} your message has been submitted succesfully !')
        new_message.save()
        
        
    return render(request, 'portfolioapp/index.html')