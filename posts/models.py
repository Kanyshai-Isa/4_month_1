from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

"""
create table post (id serial primary key autoincrement, titlevarchar (255) )
"""

"""
select * from posts: --> Post.objects.all()
"""

""" 
select 1 from posts where id=1; --> Post.objects.get(id=1)
"""

"""
select * from posts where title ILIKE '%test%'; --> Post.objects.filter(title_incontains='test')
"""

"""
insert into posts(titltle, content) values ("title", "content"); --> Post.object.create(title="title", content="content")
"""
"""
select * from from posts order by rate title; --> Post.objects.all().order_by("-rate")
"""

class Category (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=1000, null=True, blank=True)
    rate = models.IntegerField(default=0)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.title}"
