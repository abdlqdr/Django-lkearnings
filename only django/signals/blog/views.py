from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group
# Home View
def Home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

# About View
def About(request):
    return render(request, 'blog/about.html')

# Contact View
def Contact(request):
    return render(request, 'blog/contact.html')

# Dashboard View
def Dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        ip = request.session.get('ip', 0)
        return render(request, 'blog/dashboard.html', {'posts': posts, 'full_name': full_name, 'groups':gps, 'ip':ip})
    else:
        return HttpResponseRedirect('/login/')

# signup View
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!!! You have become an Author... Login Now')
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            return HttpResponseRedirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form':form})

# Login View
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

# logout View
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# Add Post View
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title, desc=desc)
                pst.save()
                messages.success(request, 'Post Added successfully')
                form = PostForm()
        else:        
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

# update Post View
def update_post(request, id):
    if request.user.is_authenticated:
        if request.user.is_authenticated:
            if request.method == 'POST':
                pi = Post.objects.get(pk=id)
                form = PostForm(request.POST, instance=pi)
                if form.is_valid():
                    messages.success(request, 'Post updated successfully')
                    form.save()
            else:
                pi = Post.objects.get(pk=id)
                form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

# Delete Post View
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            messages.success(request, 'Post deleted successfully..!!!')
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
