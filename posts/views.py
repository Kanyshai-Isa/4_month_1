from django.shortcuts import render, HttpResponse
from random import randint
from posts.models import Post

def home_view(request):
    return render(request, "base.html")

# Create your views here.

def test_view(request):
    return HttpResponse(f"Рвндомное число: {randint(1,1000)}")

def html_view(request):
    return render(request, "base.html")

def posts_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/posts_list.html", context={"posts": posts})

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/post_detail.html", context={"post":post})

    

