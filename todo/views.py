from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def home(request):
    if request.method == 'POST':
        tasks = Task.objects.all()
        tasku = request.POST.get('task')
        tosave = Task(task=tasku)
        tosave.save()
        return render(request,'home.html',context={'title':'Home','data':tasks})
    tasks = Task.objects.all()
    return render(request,'home.html',context={'title':'Home','data':tasks})

def remover(request,whom):
    which = Task.objects.get(id=whom)
    which.completed=True
    which.save()
    return redirect('home')
