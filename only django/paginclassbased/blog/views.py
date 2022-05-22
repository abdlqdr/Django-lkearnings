from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.http import Http404


# Create your views here.
class PostListview(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['id']
    paginate_by = 3
    paginate_orphans = 2
    
    def get_context_data(self, **kwargs):
        try:
            return super(PostListview, self).get_context_data(**kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(PostListview, self).get_context_data(**kwargs)
        
    # def paginate_queryset(self, queryset):
    #     try:
    #         return super(PostListview, self).get_queryset(queryset)
    #     except Http404:
    #         self.kwargs['page'] = 1
    #         return super(PostListview, self).get_queryset(queryset)
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'