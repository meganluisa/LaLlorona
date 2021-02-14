from django.shortcuts import render
from .models import Food

# Create your views here.
def food_detail_view(request, *args, **kwargs):
    obj = Food.objects.get(id=1)
    context = {
        'title': obj.title,
        'description': obj.description,
        'image_url': obj.image_url,
        'featured': obj.featured
    }
    return render(request, "product/detail.html", context)