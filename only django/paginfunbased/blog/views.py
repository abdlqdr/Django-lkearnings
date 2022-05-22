from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def Post_list(request):
    all_post = Post.objects.all().order_by('id')
    print('all_post', all_post)
    paginator = Paginator(all_post, 3, orphans=2)
    print('paginator', paginator)
    page_number = request.GET.get('page')
    print('Page_number', page_number)
    page_obj = paginator.get_page(page_number)
    print('Page_obj',page_obj)
    return render(request, 'blog/home.html', {'pages':page_obj})