from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'base_login.html')
    else:
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        userR = User.objects.get(email=email)

        user = auth.authenticate(user=userR.username, password=password)

        if user is not None and user.is_active:
            return HttpResponseRedirect("/site/base_loggedin")
        return render(request, 'base_login.html')


def register(request):
    return render(request, 'base_register.html')


def error(request):
    return render(request, 'base_error.html')
