from django.contrib import admin

# Register your models here.

from posts.models import Post, Category, Tag

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
