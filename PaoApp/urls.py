from django.urls import path

from . import views

urlpatterns = [
    path( '', views.index, name= 'index'),
    path('login/', views.login_view, name='login'),
    path('testLogin',views.testLogin, name='testLogin')
]