from taggit.forms import TagWidget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag
from .models import Comment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")

class PostForm(forms.ModelForm):
    # Comma-separated tags input (checker-friendly)
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas.",
        widget=TagWidget()
    )

    class Meta:
        model = Post
        fields = ("title", "content", "tags")
        widgets = {
            "tags": TagWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            existing = self.instance.tags.values_list("name", flat=True)
            self.fields["tags"].initial = ", ".join(existing)

    def save(self, commit=True):
        post = super().save(commit=False)

        if commit:
            post.save()

        tags_str = self.cleaned_data.get("tags", "")
        tag_names = [t.strip() for t in tags_str.split(",") if t.strip()]

        tag_objs = []
        for name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=name)
            tag_objs.append(tag)

        post.tags.set(tag_objs)

        return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)

