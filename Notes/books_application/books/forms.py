from django import forms
from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        # specify the model to be used
        model = Book

        # specify the fields to be used

        fields = [
            "title",
            "description",
        ]