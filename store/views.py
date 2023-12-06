from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from store.models import product, pannier, article


def index(request):
    products = product.objects.all()
    return render(request, 'store/index.html', context={"prod": products})

def detail_produit(requeste, slug):
    pro = get_object_or_404(product, slug=slug)
    return render(requeste, 'store/detail.html', context={"pro": pro})
def detail_article(request, slug):
   user = request.user
   prod = get_object_or_404(product, slug=slug)
   pan, _ = pannier.objects.get_or_create(user=user)
   order, created = pannier.objects.get_or_create(user=user,
                                                  product=prod)
   if created:
       pannier.article.add(order)
       pannier.save()
   else:
       article.Qte += 1
       article.save()

   return redirect(reverse("detail", kwargs={"slug" : slug}))