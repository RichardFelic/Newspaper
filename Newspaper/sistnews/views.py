from unicodedata import name
from urllib import request
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from sistnews.models import *
from sistnews.forms import *
from http.client import HTTPResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group

# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','candidato','empleado'])
def home(request):
    noticia = Noticia.objects.all()
    
    return render(request, 'sistnews/homenews.html',{'noticia':noticia})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','empleado'])
def noticia(request):
    noticia = Noticia.objects.all()
    return render(request, 'sistnews/noticia.html', {'noticia':noticia})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','empleado'])
def tablero(request):
    noticia = Noticia.objects.all()
    return render(request, 'sistnews/tablero.html', {'noticia':noticia})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','empleado'])
def registrarNoticia(request):
    form = NoticiaForm()
    if request.method == "POST":
        form = NoticiaForm(request.POST or None, request.FILES)
        form.instance.createdBy = request.user
        if form.is_valid():
            form.save()
            return redirect('/noticia')
        else:
            return HTTPResponse("""Something went wrong. Please reload 
            the webpage by clicking <a href="{{url:'noticia'}}> Reload</a>"
            """)
    else:
        return render(request, 'sistnews/registrarnoticia.html', {'form':form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','empleado'])
def registrarNoticiaEmpleado(request):
    form = NoticiaForm()
    if request.method == "POST":
        form = NoticiaForm(request.POST or None, request.FILES)
        form.instance.createdBy = request.user
        if form.is_valid():
            form.save()
            return redirect('/userPage')
        else:
            return HTTPResponse("""Something went wrong. Please reload 
            the webpage by clicking <a href="{{url:'noticia'}}> Reload</a>"
            """)
    else:
        return render(request, 'sistnews/registrarnoticia.html', {'form':form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','empleado'])
def editarNoticia(request, pk,):
    noticia = Noticia.objects.get(id=pk)
    data = {'form': NoticiaForm(instance=noticia)
    }
    if request.method == 'POST':
        form = NoticiaForm(data=request.POST or None, instance=noticia, 
        files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/noticia')
        data["form"] = form
    return render(request, 'sistnews/editarnoticia.html', data)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','empleado'])
def borrarNoticia(request, pk):             
    noticia = Noticia.objects.get(id=pk)
    if request.method == 'POST':
        noticia.delete()
        return redirect('/noticia')
    context = {'noticia':noticia}
    return render(request, 'sistnews/borrarnoticia.html', context)   

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','candidato','empleado'])
def detalleNoticia(request, pk):
    noticia = Noticia.objects.all().get(id=pk)
    context = {'noticia':noticia}
    return render(request, 'sistnews/detallenoticia.html', context) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','candidato','empleado'])
def noticiapublico(request, pk):
    noticia = Noticia.objects.all().get(id=pk)
    context = {'noticia':noticia}
    return render(request, 'sistnews/noticiapublico.html', context) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def clasificacionpublico(request, pk):
    noticia = Noticia.objects.all()
    clasificacion = Clasificacion.objects.all()
    context = {'clasificacion':clasificacion,'noticia':noticia}
    return render(request, 'sistnews/clasificacionpublico.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','candidato','empleado'])
def general(request):
    noticia = Noticia.objects.all()
    context = {'noticia':noticia}
    return render(request, 'sistnews/Categoria/General.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','candidato','empleado'])
def tecnologia(request):
    noticia = Noticia.objects.filter(clasificacion="Tecnologia").all()
    context = {'noticia':noticia}
    return render(request, 'sistnews/Categoria/Tecnologia.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','candidato','empleado'])
def salud(request):
    noticia = Noticia.objects.filter(clasificacion="Salud").all()
    context = {'noticia':noticia}
    return render(request, 'sistnews/Categoria/Salud.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','candidato','empleado'])
def ciencia(request):
    noticia = Noticia.objects.filter(clasificacion="Ciencia").all()
    context = {'noticia':noticia}
    return render(request, 'sistnews/Categoria/Ciencia.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','candidato','empleado'])
def cultura(request):
    noticia = Noticia.objects.filter(clasificacion="Cultura").all()
    context = {'noticia':noticia}
    return render(request, 'sistnews/Categoria/Cultura.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','candidato','empleado'])
def negocio(request):
    noticia = Noticia.objects.filter(clasificacion="Negocio").all()
    context = {'noticia':noticia}
    return render(request, 'sistnews/Categoria/Negocio.html', context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='candidato')
            user.groups.add(group)

            messages.success(request, 'Account was created for' + username)
            return redirect('loginPage') 

    context={'form':form}
    return render(request, 'sistnews/RegisterLogin/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password1')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
            else:
                messages.info(request, 'El Nombre de Usuario o la Contraseña está incorrecta')
                
    context={}
    return render(request, 'sistnews/RegisterLogin/login.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('loginPage')

#User
@login_required(login_url='login')
@allowed_users(allowed_roles=['empleado'])
def userPage(request):
    #candidatos = Candidato.objects.filter(createdBy=request.user)
    noticia = Noticia.objects.filter(createdBy=request.user)

    #context={'candidato': candidato}
    return render(request,'sistnews/User.html', {'noticia':noticia})