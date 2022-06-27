from audioop import reverse
from dataclasses import fields
from msilib.schema import ListView
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView


from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return super().get_queryset().filter(status="published")

    # template_name = 'blog/post_list.html'


class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    # template_name = 'blog/post_form.html'


class PostDetailView(DetailView):
    model = Post
    # template_name = 'blog/post_detail.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all") 
    # template_name = 'base.html'


class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    # template_name = 'blog/post_confirm_delete.html'
