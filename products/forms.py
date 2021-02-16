from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
            'title', 'description', 'price', 'image_url'
        ]