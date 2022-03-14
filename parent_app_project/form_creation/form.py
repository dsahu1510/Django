from dataclasses import field
from pyexpat import model
from django import forms
from .models import main_form

class form_info(forms.Form):
    class Meta:
        model = main_form


        field = [
            "title",
            "desc"
        ]