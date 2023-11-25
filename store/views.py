from django.shortcuts import render,get_object_or_404
from store.models import product
from django.http import HttpResponse

def index(request):
    products = product.objects.all()
    return render(request, 'store/index.html', context={"prod":products})

def detail_produit(requeste, slug):
    pro= get_object_or_404(product, slug=slug)
    return render(requeste,'store/detail.html', context={"pro":pro})
