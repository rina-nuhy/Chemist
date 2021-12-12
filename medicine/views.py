from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request,'chemist/index.html')

def products(request):
    return render(request,'chemist/products.html')

def search(request):
    pass

def about(request):
    return render(request, 'chemist/about-us.html')

def contact(request):
    return render(request, 'chemist/contact.html')

def search(request):
    if 'productsearch' in request.GET and request.GET["productsearch"]:
        product = request.GET.get("productearch")
        searched_images = Medicine.search_by_product(product)
        message = f"{product}"
        print(searched_images)
        return render(request, 'chemist/search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any product"
        return render(request, 'chemist/search.html', {"message": message})    