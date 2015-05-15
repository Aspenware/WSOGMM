from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib import auth
<<<<<<< HEAD
from django.views.generic import RedirectView
=======
from django.contrib.auth.models import User
>>>>>>> e3a100076f4b52b7de631e7ae670f225b16c6186

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

        user = auth.authenticate(user=userR.username, password=password)

        if user is not None and user.is_active:
            return RedirectView.as_view(url="/site/login")(request)
        return render(request, 'base_login.html')


def logout(request):
    if request.user is not None and request.user.is_authenticated():
        auth.logout(request)

    return RedirectView.as_view(url='/site/login')(request)



def register(request):
    return render(request, 'base_register.html')


def error(request):
    return render(request, 'base_error.html')
