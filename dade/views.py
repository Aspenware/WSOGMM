from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib import auth
from django.views.generic import RedirectView

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'base_login.html')
    else:
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=email, password=password)

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
