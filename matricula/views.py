from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
	return render(request,'index.html')

def registro(request):
	if request.method == 'POST':
		form = AlumnoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

def index2(request):
	alumnos = Alumno.objects.all()

	form = AlumnoForm()

	if request.method =='POST':
		form = AlumnoForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, "registro.html")
		return redirect('/')


	context = {'alumnos':alumnos, 'form':form}
	return render(request, 'list.html', context)

def matricularAlum(request, pk):
	alumno = Alumno.objects.get(id=pk)

	form = AlumnoForm(instance=alumno)

	if request.method == 'POST':
		form = AlumnoForm(request.POST, instance=alumno)
		if form.is_valid():
			form.save()
			return redirect('/index2/')

	context = {'form':form}

	return render(request, 'matricular_alum.html', context)

def borrarAlum(request, pk):
	item = Alumno.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/index2/')

	context = {'item':item}
	return render(request, 'borrar_alum.html', context)

def Contacto(request):
	if request.method == 'POST':
		nm = request.POST.get('nombreu')
		email = request.POST.get('correou')
		txt = request.POST.get('mensajeu')
		print(nm,email,txt)
		contacto = Contacto(nombreu = nm, correou = email, mensajeu = txt)
		contacto.save()
		return redirect('/')
	return render(request,'registro.html')