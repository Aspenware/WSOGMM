from django.shortcuts import render
from django.contrib import auth
from django.views.generic import RedirectView
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    if request.method == 'GET':
      if request.user.is_authenticated():
        return render(request, 'base.html')
      else:
        return render(request, 'base_login.html')
    else:
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        userR = User.objects.get(email=email)

        user = auth.authenticate(username=userR.username, password=password)
        print request.user
        if user is not None and user.is_active:
            auth.login(request, user)
            return RedirectView.as_view(url="/site/login")(request)
        print request.user
        return render(request, 'base_login.html')

def logout(request):
    if request.user is not None and request.user.is_authenticated():
        auth.logout(request)
    return RedirectView.as_view(url='/site/login')(request)

def register(request):
    return render(request, 'base_register.html')

def error(request):
    return render(request, 'base_error.html')

def index(request):
    return render(request, 'base.html')

def event(request):
    return render(request, 'base.html')
