from django.contrib import admin

# Register your models here.

from posts.models import Post, Category, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "rate")
    list_editable = ("category",)


admin.site.register(Category)
admin.site.register(Tag)
