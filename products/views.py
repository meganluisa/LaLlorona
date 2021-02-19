from django.shortcuts import render
from .models import Food
from .forms import FoodForm, RawFoodForm

def food_create_view(request):
    my_form = RawFoodForm()
    context = {
        "form": my_form
    }
    return render(request, "product/product_create.html", context)

# def food_create_view(request):
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#     context = {}
#     return render(request, "product/product_create.html", context)

# def food_create_view(request):
#     form = FoodForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = FoodForm()
#     context = {
#         'form': form
#     }
#     return render(request, "product/product_create.html", context)

# Create your views here.
def food_detail_view(request, *args, **kwargs):
    obj = Food.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'image_url': obj.image_url,
    #     'featured': obj.featured
    # }
    context = {
        'object': obj
    }
    return render(request, "product/product_detail.html", context)

