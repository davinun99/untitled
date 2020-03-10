from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pyrebase
from django.contrib import auth
from django.views.generic.base import TemplateView
config = {
    'apiKey': "AIzaSyAbCiMgh8az4COYBvq038jbrvVGA16oCeo",
    'authDomain': "poliproyecto-6dfb4.firebaseapp.com",
    'databaseURL': "https://poliproyecto-6dfb4.firebaseio.com",
    'projectId': "poliproyecto-6dfb4",
    'storageBucket': "poliproyecto-6dfb4.appspot.com",
    'messagingSenderId': "562557261320",
    'appId': "1:562557261320:web:64f3792e7ca3608c1463bd",
    'measurementId': "G-GED6N0CHKC"
}
firebase = pyrebase.initialize_app(config)

authfb = firebase.auth()

# Create your views here.


def index(request):
    return HttpResponse("Hola")


def login( request ):
    return render( request, 'PaoApp/login.html', { })


def IZItestLogin( request ):
    email = request.POST['email']
    password = request.POST['password']
    user = authfb.sign_in_with_email_and_password(email, password)
    session_id = user.idToken

    message = 'Credenciales invalidas'
    context = {
        'userFirebaseData': user
    }
    return render(request, 'PaoApp/testLogin.html', context)

def testLogin( request ):
    email = request.POST['email']
    password = request.POST['password']
    try:
        user = authfb.sign_in_with_email_and_password(email, password)

    except:
        message = 'Credenciales invalidas'
        return render( request, 'PaoApp/login.html',{ 'error_message' : message } )
    print(user)
    context = {
        'userFirebaseData': user
    }
    session_id = user['idToken']
    request.session['uid'] = str( session_id )
    return render( request, 'PaoApp/testLogin.html', context)

def logout( request ):
    auth.logout( request )
    return render( request, 'PaoApp/login.html',{})
