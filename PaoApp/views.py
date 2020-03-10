from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView


# Create your views here.


def index(request):
    return HttpResponse("Hola")


def login( request ):
    return render( request, 'PaoApp/login.html', { })
def testLogin( request ):
    context = {
        'username' : request.POST['username'],
        'password' : request.POST['password']
    }
    return render( request, 'PaoApp/testLogin.html', context)
