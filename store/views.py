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
    produit=get_object_or_404(product, slug=slug)

    # Vérifiez si l'article existe dans le panier
    order, created = article.objects.get_or_create(utilisateur=user, produit=prod, order=False)
    if produit.stock > 0:
      if created:
           pan.article.add(order)
      else:
        order.Qte += 1
        order.save()
        produit.stock -= 1
        produit.save()
      return redirect(reverse("detail", kwargs={"slug": slug}))

    else:
        return redirect(reverse("index"))

def affiche_pannier(request):
    pan=get_object_or_404(pannier, user=request.user)
    return render("store/Article.html", context={"pan":pannier.article})
