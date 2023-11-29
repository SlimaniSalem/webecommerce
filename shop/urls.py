
from django.contrib import admin
from django.urls import path
from store.views import index, detail_produit
from django.conf.urls.static import static
from shop import settings
from user_cont.views import user_log,user_dec,login


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('user/',user_log,name='user'),
    path('connexion/',login,name='connecter'),
    path('déconnxion', user_dec,name='deco'),
    path('product/<str:slug>/', detail_produit, name="detail"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
