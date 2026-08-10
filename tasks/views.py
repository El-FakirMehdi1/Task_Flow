from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Task,Category
from .Form import TaskForm,RegisterForm
# Create your views here.
@login_required
def home(request):

    categories = Category.objects.all()
    user_tasks = Task.objects.filter(user=request.user)
    Tasks = user_tasks
    search = request.GET.get("search")
    category = request.GET.get("category")
    priority = request.GET.get("priority")
    
    if search:

        Tasks = Tasks.filter(

            Q(title__icontains=search)

        )
    
    if category:

        Tasks = Tasks.filter(
       category_id=category
    )
    if priority:
        Tasks = Tasks.filter(priority=priority)
    
    total_tasks = user_tasks.count()

    total_completed = user_tasks.filter(
        Completed=True
    ).count()

    total_pending = user_tasks.filter(
        Completed=False
    ).count()

    total_high_priority = user_tasks.filter(
        priority="H"
    ).count()
    return render(request, "Tasks/home.html", context ={
        "Tasks" : Tasks,
        "total_tasks": total_tasks,
        "total_completed": total_completed,
        "total_pending": total_pending,
        "total_high_priority": total_high_priority,
        "categories":categories,
        "priority" : priority,
    })
@login_required
def add_task(request):
   if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            form.save()
            messages.success(request,"Task Added successfully!")
            
            return redirect("home")
   else:
        form = TaskForm() 

   return render(request,"Tasks/add_tasks.html" , {"form" : form})
@login_required
def edit_task(request,id):
    task = get_object_or_404(Task,id=id)
    if request.method == 'POST':
        form =TaskForm(
            request.POST,
            instance = task
        )
        if form.is_valid():
            form.save()
            messages.success(request,"Task Updated successfully!")
            return redirect("home")
    else :
        form = TaskForm(instance=task)
    return render(request,"Tasks/edit_tasks.html",{"form" : form})
@login_required
def delete_task(request,id):
    task = get_object_or_404(Task,id =id)
    if request.method=='POST':
        task.delete()
        messages.success(request,"Task Deleted successfully!")
        return redirect("home")
    return redirect('home')

def login_user(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect("home")

    else:

        form = AuthenticationForm()
    return render(request,'Tasks/login.html',{'form':form})

def register_user(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    else:

        form = RegisterForm()

    return render(
        request,
        "Tasks/register.html",
        {
            "form": form
        }
    )
def logout_user(request):

    logout(request)

    return redirect("login")