from .models import *
# from django.shortcuts import render,redirect
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic import DetailView


# To retrieve Company details
def index(request):
    projects = Project.objects.all().order_by('-id')
    comments = Comment.objects.all().order_by('-id')
    if request.method == 'POST':  
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('index')
    
    else:
        form = CommentForm()
    return render(request, "index.html", {"projects": projects, 'form':form, "comments":comments})

def like(request,project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        user = request.user
        if user in project.likes.all():
            project.likes.remove(user)
        else:
            project.likes.add(user)

    return redirect('/', project_id=project.id)

@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    
    return render(request, "profile.html", {"profile": profile})


@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    return render(request, 'update_profile.html', {"form":form})

@login_required(login_url='/accounts/login/')

@login_required
def comments(request,project_id):
  form = CommentForm()
  project = Project.objects.filter(id = project_id).first()
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit = False)
      comment.user = request.user
      comment.project = project
      comment.save() 
    return redirect('index')
  




    
