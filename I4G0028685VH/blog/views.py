from audioop import reverse
from dataclasses import fields
from msilib.schema import ListView
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from I4G0028685VH.blog.models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'


class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    template_name = 'post_form.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all") 
    template_name = 'base.html'


class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    template_name = 'post_confirm_delete.html'
