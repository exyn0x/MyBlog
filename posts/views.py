from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.

def home(request):
    posts = list(models.Post.objects.all())
    context = {'posts': posts}
    return render(request, 'home.html', context)

def get_post(request, post_id: int):
    # post = models.Post.objects.filter(id=post_id).first()
    post = get_object_or_404(models.Post, id=post_id)
    context = {'post': post}
    return render(request, 'post.html', context)
