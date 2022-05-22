from django.shortcuts import render
from .models import Post, Page, Song, User

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def show_user_data(request):
    data1 = User.objects.all()
    data2 = User.objects.filter(email='contact@geekyshows.com')
    data3 = User.objects.filter(mypage__page_cat='programming')
    data4 = User.objects.filter(mypost__post_publish_date='2022-1-2')
    data5 = User.objects.filter(mysong__song_duration=4)
    return render(request, 'myapp/user.html', {'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4, 'data5':data5})

def show_page_data(request):
    data1 = Page.objects.all()
    data2 = Page.objects.filter(page_cat='programming')
    data3 = Page.objects.filter(user__email='contact@geekyshows.com')
    return render(request, 'myapp/page.html', {'data1':data1, 'data2':data2, 'data3':data3})

def show_post_data(request):
    data1 = Post.objects.all()
    data2 = Post.objects.filter(post_publish_date='2022-1-2')
    data3 = Post.objects.filter(user__username='sonam')
    return render(request, 'myapp/post.html', {'data1':data1, 'data2':data2, 'data3':data3})

def show_song_data(request):
    data1 = Song.objects.all()
    data2 = Song.objects.filter(song_duration=4)
    data3 = Song.objects.filter(user__username='sonam')
    return render(request, 'myapp/Song.html', {'data1':data1, 'data2':data2, 'data3':data3})