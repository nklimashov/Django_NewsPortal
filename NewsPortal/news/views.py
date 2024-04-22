from datetime import datetime
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .filters import NewsFilters
from .models import Post
from .forms import PostForm


class PostsList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.order_by('-creation_date')

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     self.filterset = NewsFilters(self.request.GET, queryset)
    #     return self.filterset.qs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filterset'] = self.filterset
    #     return context


class PostsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostSearch(ListView):
    model = Post
    ordering = 'title'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilters(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        return context



class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_type = 'NW'
        post.save()
        return super().form_valid(form)


class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'art_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_type = 'AR'
        post.save()
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')


class ArticleUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'art_edit.html'


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'art_delete.html'
    success_url = reverse_lazy('post_list')




    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['creation_date'] = datetime.utcnow()
    #     return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['creation_date'] = datetime.utcnow()
    #     return context

    # return Post.objects.order_by('-creation_date')