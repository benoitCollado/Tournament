from django.shortcuts import render
from django.views import generic
from django.utils import timezone


from .models import Post



class IndexView(generic.ListView):
  template_name = 'blog/index.html'
  context_object_name = 'posts'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Accueil Blog'
    context['title_application'] = 'Blog'
    return context

  def get_queryset(self):
    return Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
  model = Post
  template_name = 'blog/detail.html'
  context_object_name = 'post'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = context['post'].title
    context['title_application'] = 'Blog'
    return context

  def get_queryset(self):
    return Post.objects.filter(pub_date__lte=timezone.now())
