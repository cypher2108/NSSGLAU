from django.shortcuts import render, redirect

# Create your views here.
from base.models import Contact, Post


def home(request):
    error = ''
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        try:
            Contact.objects.create(name=name, subject=subject, email=email, message=message)
            error = 'no'
        except:
            error = 'yes'

    posts = Post.objects.all()
    x = {'error': error, 'posts': posts}
    return render(request, 'base/home.html', x)


def about(request):
    return render(request, 'base/about.html')


def contact(request):
    return render(request, 'base/contact.html')