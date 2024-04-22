from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(min_length=20, strip=True)

    class Meta:
        model = Post
        fields = [
            'title',
            'post_author',
            'content',
        ]

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("content")
        name = cleaned_data.get("title")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data
