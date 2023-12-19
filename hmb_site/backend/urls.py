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
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
