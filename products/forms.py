from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
            'title', 'description', 'price', 'image_url'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            return title
        else:
            raise forms.ValidationError("This is not a valid title")

class RawFoodForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "placeholder": "Your description",
                                "class": "new-class-name two",
                                "id": "my-id-for-textarea",
                                "rows": 5,
                                "cols": 30
                            }
                        )
    )
    price = forms.DecimalField()
