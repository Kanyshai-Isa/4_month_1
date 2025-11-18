from django import forms
from posts.models import Category, Post, Tag

class PostForm(forms.Form):
    image = forms.ImageField(label="Image")
    title = forms.CharField(label="Title", max_length=250)
    content = forms.CharField(label="Content", max_length=1000)
    rate = forms.IntegerField(label="Rate")

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title.lower() == "javascript":
            raise forms.ValidationError("JavaScript is a bad language")
        return title
    
    def clean_image(self):
        cleaned_data = super().clean()
        image = cleaned_data.get("image")
        name = image.name.split(".")[-1]
        if name not in ["jpg", "jpeg"]:
            raise forms.ValidationError("Only .jpg and .jpeg images are allowed")
        return image
    
class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("image", "title", "content", "rate")

class SearchForm(forms.Form):
    search = forms.CharField(label="Search", required=False)
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    tags_ids = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    orderings = (
        ("rate", "По оценкам"),
        ("-rate", "По оценкам по убыванию"),
        ("title", "По названию"),
        ("-title", "По нпазванию по убыванию"),
        ("created_at", "По дате создания"),
        ("-created_at", "По дате создания по убыванию"),
        ("updated_at", "По дате обновления"),
        ("-updated_at", "По дате обновления по убыванию"),
        (None, "Без сортировки"),
    )
    ordering = forms.ChoiceField(choices=orderings, required=False)