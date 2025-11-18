from django.shortcuts import render, HttpResponse, redirect
from random import randint
from posts.models import Post
from posts.forms import PostForm2, SearchForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

"""
posts = [post1, post2, post3,post4,post5,post6,post7,post8,post9,post10....post20]
limit = 4
pages = 20/4 = 5
page = 3
start = (page - 1 ) *limit = 8
end = page * limit = 12
"""


def home_view(request):
    if request.method == "GET":
        return render(request, "base.html")

# Create your views here.

def test_view(request):
    return HttpResponse(f"Рвндомное число: {randint(1,1000)}")

def html_view(request):
    if request.method == "GET":
        return render(request, "base.html")

@login_required(login_url="/login/")
def posts_list_view(request):
    posts = Post.objects.all()
    form = SearchForm()
    limit = 3
    if request.method == "GET":
        query_params = request.GET
        search = query_params.get("search")
        category_id = query_params.get("category_id")
        tags_ids = query_params.getlist("tags_ids")
        ordering = query_params.get("ordering")
        page = int(query_params.get("page", 1))
        if search:
            posts = posts.filter(Q(Q(title__icontains=search) | Q(content__icontains=search)))
        if category_id:
            posts = posts.filter(category_id=category_id)
        if tags_ids:
            posts = posts.filter(tags__id__in=tags_ids).distinct()
        if ordering:
            posts = posts.order_by(ordering)
        if page:
            max_pages = posts.count() / limit
            if round(max_pages) < max_pages:
                max_pages = round(max_pages) + 1
            else:
                max_pages = round(max_pages)
            start = (page - 1) * limit
            end = page * limit
            posts = posts[start:end]
        return render(request, "posts/posts_list.html", context={"posts": posts, "form": form, "max_pages": range(1, max_pages+1)})

@login_required(login_url="/login/")
def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, "posts/post_detail.html", context={"post":post})

@login_required(login_url="/login/")  
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