from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpRequest
from blogs.forms import LoginForm, SignupForm ,uploadBlog 
from . models import *
from django.urls import reverse
from django.contrib.auth import authenticate ,login , logout 


def homepage(request):
    allBlogs=Blog.objects.all()
    return render(request, 'home_page.html', {'allBlogs':allBlogs})


def login_page(request):
    allBlogs=Blog.objects.all()
    if request.user.is_authenticated:
        return redirect(reverse('show_blog'))

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            user = User.objects.filter(username=username).first()
            if user:
                login(request, user)
                return redirect(reverse('show_blog'))
            else:
                return redirect(reverse('homepage'))
    else:
        form = LoginForm()  
    
    return render(request, 'login_page.html', {'form': form ,'allBlogs':allBlogs })


def logout_page(request):
    logout(request)
    return render(request, 'logout.html')
    

def signup(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user_img=request.FILES.get('user_img')
            gender=request.POST.get('gender')
            userObj=User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        
            userinfoObj=Userinfo.objects.create(user_img=user_img,username=username,user=userObj,first_name=first_name,last_name=last_name,
                      gender=gender,email=email,phone_number=phone_number,password=password)
        return redirect(reverse('homepage'))
    return render(request,'signup_page.html')


def upload_blog(request):
    
    if request.method=='POST':
        form=uploadBlog(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            blog=form.cleaned_data['blog']
            post_img = request.FILES.get('post_img')
            timestamp = request.POST.get('timestamp')
            user_info = Userinfo.objects.get(user=request.user)
            blog_obj = Blog(title=title, blog=blog, post_img=post_img, timestamp=timestamp, user=user_info)
            blog_obj.save()
            return redirect(reverse('show_blog'))
    return render(request, 'upload_blog.html')


def show_blog(request):
    user_info = Userinfo.objects.get(user=request.user)
    userblogs=Blog.objects.filter(user=user_info).order_by('-id')

    return render(request ,'bloger_page.html',{'userblogs':userblogs})


def change(request,blog_id):
    userblogs = Blog.objects.get(id=blog_id)
    return render(request, 'change.html', {'userblogs':userblogs})


def update(request, blog_id):
     userblogs = Blog.objects.get(id=blog_id)
     if request.method == 'POST':
        form=uploadBlog(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            blog=form.cleaned_data['blog']
            post_img = request.FILES.get('post_img')
        
            if title:
                userblogs.title = title
            if blog:
                userblogs.blog = blog
            if post_img:
                userblogs.post_img = post_img
            userblogs.save()
        return redirect(reverse('show_blog'))
    

def delete(request, blog_id):
    userblogs = Blog.objects.get(id=blog_id)
    userblogs.delete()
    return redirect(reverse('show_blog'))