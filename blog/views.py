from django.shortcuts import render
from .models import Post

def showeblog (request):
    p=Post.objects
    return render(request, 'blog/blog.html',{'p':p})
