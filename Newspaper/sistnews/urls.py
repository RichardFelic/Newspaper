from unicodedata import name
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('tablero/', views.tablero, name='tablero'),
    path('noticia/', views.noticia, name='noticia'),

    #CRUD NOTICIAS
    path('registrarNoticia/', views.registrarNoticia, name='registrarNoticia'),
    path('editarNoticia/<str:pk>/', views.editarNoticia, name='editarNoticia'),
    path('borrarNoticia/<str:pk>/', views.borrarNoticia, name='borrarNoticia'),
    path('detalleNoticia/<str:pk>/', views.detalleNoticia, name='detalleNoticia'),

    #Clasificaciones
    path('general/',views.general, name='general'),
    path('tecnologia/',views.tecnologia, name='tecnologia'),
    path('salud/',views.salud, name='salud'),
    path('ciencia/',views.ciencia, name='ciencia'),
    path('cultura/',views.cultura, name='cultura'),
    path('negocio/',views.negocio, name='negocio'),

    #Tira informacion
    path('noticiapublico/<str:pk>/', views.noticiapublico, name='noticiapublico'),
    path('clasificacionpublico/<str:pk>/', views.clasificacionpublico, name='clasificacionpublico'),

    #Login y Register
    path('registerPage/', views.registerPage, name='registerPage'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),
    path('userPage/', views.userPage, name='userPage'),
    path('registrarNoticiaEmpleado/', views.registrarNoticiaEmpleado, name='registrarNoticiaEmpleado'),
]