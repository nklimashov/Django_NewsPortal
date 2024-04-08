from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView

from .models import Post

from pprint import pprint
class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'

    def get_queryset(self):
        return Post.objects.order_by('-creation_date')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['creation_date'] = datetime.utcnow()
    #     return context


class PostsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['creation_date'] = datetime.utcnow()
    #     return context
