from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "category", "image"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "Enter item title",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full px-3 py-2 border rounded-lg h-32 resize-none focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "Describe the item in detail",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500"
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "w-full px-3 py-2 border rounded-lg file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-orange-50 file:text-orange-700 hover:file:bg-orange-100"
                }
            ),
        }
