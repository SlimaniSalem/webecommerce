
from django.contrib import admin
from django.urls import path
from store.views import index, detail_produit
from django.conf.urls.static import static
from shop import settings


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('product/<str:slug>/', detail_produit),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
