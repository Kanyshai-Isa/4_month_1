from django.db import models

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

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=1000, null=True, blank=True)
    rate = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.content}"
