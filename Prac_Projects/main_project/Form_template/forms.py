from dataclasses import field
from pyexpat import model
from django import forms
from . models import newBooks

class bookForm (forms.ModelForm):

    # meta information is being used meta means raw data and specify the model to be used
    class Meta:
        model = newBooks

        # specify the fields to be used from ur model.py

        field = [
            "Book_title",
            "Book_desc",
        ]
