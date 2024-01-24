from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
    path('category-title/<val>', views.CategoryTitle.as_view(), name='category_title'),
    path('product/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('checkout/', views.show_cart, name='checkout'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('delivery/', views.delivery, name='delivery'),
    path('workout/', views.workout, name='workout'),
    path('news/', views.NewsView.as_view(), name='news'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
