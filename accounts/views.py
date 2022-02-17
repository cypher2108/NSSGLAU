from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
# Create your views here.


def user_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pword']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    d = {'error': error}
    return render(request, 'accounts/login.html', d)

def user_logout(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        logout(request)
        return redirect('home')


def register(request):
    return render(request, 'accounts/register.html')
