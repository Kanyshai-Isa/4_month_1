from django.shortcuts import render, HttpResponse, redirect
from random import randint
from posts.models import Post
from posts.forms import PostForm2

def home_view(request):
    if request.method == "GET":
        return render(request, "base.html")

# Create your views here.

def test_view(request):
    return HttpResponse(f"Рвндомное число: {randint(1,1000)}")

def html_view(request):
    if request.method == "GET":
        return render(request, "base.html")

def posts_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, "posts/posts_list.html", context={"posts": posts})

def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, "posts/post_detail.html", context={"post":post})

    
def post_create_view (request):
    if request.method == "GET":
        form = PostForm2()
        return render(request, "posts/post_create.html", context={"form": form})
    if request.method == "POST":
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form":form})
        # title = form.cleaned_data["title"]
        # content = form.cleaned_data["content"]
        # rate = form.cleaned_data["rate"]
        # image = form.cleaned_data["image"]
        try:
            # post = Post.objects.create(title=title, content=content, rate=rate, image=image)
            form.save()
            return redirect("/posts")
        except Exception as e:
            return HttpResponse(f"Error: {e}")