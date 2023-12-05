from django.contrib import admin
from django.urls import path
from store.views import index, detail_produit, detail_article
from django.conf.urls.static import static
from shop import settings
from user_cont.views import user_log, user_dec, logine


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('user/', user_log, name='user1'),
    path('connecter/', logine, name='connecter1'),
    path('déconnxion/', user_dec, name='deco'),
    path('article/', detail_article, name='arit'),
    path('product/<str:slug>/', detail_produit, name="detail"),
    path('product/<str:slug>/add_pannier/', detail_article, name='arit'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
