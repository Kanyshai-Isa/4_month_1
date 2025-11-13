from django import forms
from posts.models import Post

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