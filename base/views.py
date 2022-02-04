from django.shortcuts import render, redirect

# Create your views here.
from base.models import Blog, Contact, Event, Post


def home(request):
    error = ''
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        print(name)
        print(subject)
        print(email)
        print(message)
        try:
            Contact.objects.create(name=name, subject=subject, email=email, message=message)
            error = 'no'
        except:
            error = 'yes'
    print(error)
    posts = Post.objects.order_by('-id')[0:3]
    main_event = Event.objects.order_by('-id')[0]
    events = Event.objects.order_by('-id')[1:3]
    main_event.date_of_event.strftime("%b")
    blogs = Blog.objects.order_by('-id')[0:3]
    x = {'error': error, 'posts': posts,'main_event': main_event, 'events': events, 'blogs': blogs}
    return render(request, 'base/home.html', x)


def about(request):
    return render(request, 'base/about.html')


def contact(request):
    return render(request, 'base/contact.html')