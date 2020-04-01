# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# from .models import Task
from .forms import TaskForm
from django.contrib import messages
# Create your views here.
from django.contrib.sessions.models import Session

def login(request):
	if request.session.has_key('is_logged'):
		return redirect('list')
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		count=User.objects.filter(username=username,password=password).count()
		if count > 0:
			request.session['is_logged'] = True
			return redirect('list')
		else:
			messages.error(request,'You are enter invalid credentials')
			return redirect('login')
	return render(request,'tasks/login.html')
def handlelogout(request):
	if request.session.has_key('is_logged'):
		del request.session['is_logged']
		return redirect('login')
	else:
		return redirect('login')
def index(request):
	if request.session.has_key('is_logged'):

		tasks = Task.objects.all()

		form = TaskForm()

		if request.method =='POST':
			form = TaskForm(request.POST)
			if form.is_valid():
				form.save()
			return redirect('/')

		messages.success(request,'You are successfully Logged In')
		context = {'tasks':tasks, 'form':form}
		return render(request, 'tasks/list.html', context)
	return redirect('login')
def updateTask(request, pk):
	if request.session.has_key('is_logged'):

		task = Task.objects.get(id=pk)

		form = TaskForm(instance=task)

		if request.method == 'POST':
			form = TaskForm(request.POST, instance=task)
			if form.is_valid():
				form.save()
				return redirect('/')

		context = {'form':form}

		return render(request, 'tasks/update_task.html', context)
	return redirect('login')

def deleteTask(request, pk):
	if request.session.has_key('is_logged'):

		item = Task.objects.get(id=pk)

		if request.method == 'POST':
			item.delete()
			return redirect('/')

		context = {'item':item}
		return render(request, 'tasks/delete.html', context)
	return redirect('login')


def printTask(request, pk):
	if request.session.has_key('is_logged'):

		item = Task.objects.get(id=pk)


		context = {'item':item}
		return render(request, 'tasks/print.html', context)
	return redirect('login')
