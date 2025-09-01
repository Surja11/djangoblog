from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.views import View
from .models import *
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm

@login_required
def password_change_view(request):
  if request.method == "POST":
    form = PasswordChangeForm(user = request.user, data = request.POST)
    if form.is_valid():
      form.save()
      print("changed")
      logout(request)
      return redirect("login")
    else: 
      print(form.errors)
  
  else:
    form = PasswordChangeForm(user = request.user)
    print("form.errors")

  print("not changed2")
  return render(request, "blogapp/password_change.html",{"form":form})


# Create your views here.
def home(request):
  blogs = Blog.objects.all()

  return render(request,'blogapp/home.html',{"blogs": blogs, "message":"All Blogs"})

@login_required
def yourblogs(request):
  user = request.user.username
  blogs = Blog.objects.filter(author = user)
  return render(request, 'blogapp/home.html', {"blogs": blogs, "message": "Your blogs"})


def loginView(request):
  if request.user.is_authenticated:
    return redirect('home')
  
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username = username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      return render(request, 'blogapp/login.html')
  else:
    return render(request,'blogapp/login.html')

def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = request.POST.get("username")

       
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        return redirect('login')
    return render(request, 'blogapp/register.html')


def logoutUser(request):
  logout(request)
  return redirect('home')

def password_reset(request):
  return render(request, 'blogapp/password_reset.html')


def password_reset_confirm(request):
  return render(request, 'blogapp/password_reset_confirm.html')


class CRUDPost(View):
  def get(self,request):
  # if request.method == 'POST':
    return render(request, 'blogapp/createblog.html')
  
  @login_required
  def post(self,request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    image = request.FILES.get('image')
    author = request.user.username

    Blog.objects.create(title = title, description = content , image = image, author = author)
    
    return render(request, 'blogapp/home.html')
  
def readBlog(request,id):
  blog = Blog.objects.get(id = id)
  return render(request,'blogapp/singlepage.html', {"blog":blog})

@login_required
def editBlog(request, id):
  blog = Blog.objects.get(id = id)
  if request.user.username == blog.author:

    if request.method =="POST":
      title = request.POST.get('title')
      description = request.POST.get('content')
      image = request.FILES.get('image')
    
    
      if image:
        blog.image = image
  
      blog.title = title
      blog.description = description
      blog.save()

      return redirect('readblog', id = blog.id)
    return render(request, 'blogapp/editpage.html',{"blog":blog})
  return redirect('home')

@login_required
def deleteBlog(request,id):

  blog = Blog.objects.get(id = id)
  if request.user.username==blog.author:
    blog.delete()
    return render(request, 'blogapp/home.html')
  return redirect('home')