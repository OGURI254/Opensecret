from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def postdefault(request):
    return render(request, 'postdefault.html')
def author(request):
    return render(request, 'author.html')
def services(request):
    return render(request, 'service.html')
def blogmasonry(request):
    return render(request, 'blogmasonry.html')
def postvideo(request):
    return render(request, 'postvideo.html')
def bloggrid(request):
    return render(request, 'bloggrid.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        ).save()

        messages.success(request, 'Details successfully processed and saved.')
        print('\n\n\n We are seeing data being saved\n\n\n')
        return redirect('index') 
    
    print('\n\n\n We are seeing this because it did not direct\n\n\n')
    return render(request, 'contact.html')



