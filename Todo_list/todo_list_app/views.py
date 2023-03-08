from django.shortcuts import render, redirect
from .models import TodoList
from django.http import JsonResponse
import json
# Create your views here.

def home(request):
	if request.method == "POST" and 'delete-btn' not in request.POST:
		task = request.POST.get('task')
		description = request.POST.get('description')
		todo_list = TodoList.objects.update_or_create(task=task.lower(), description=description.lower())
	elif request.method == "POST" and 'delete-btn' in request.POST:
		card_id = int(request.POST.get('delete-btn'))
		TodoList.objects.get(id=card_id).delete()
		return redirect('home')
	tasks = TodoList.objects.all()
	number_of_tasks = TodoList.objects.count()
	context = {'tasks': tasks, 'number_of_tasks': number_of_tasks}
	return render(request, 'todo_list_app/home.html', context)
