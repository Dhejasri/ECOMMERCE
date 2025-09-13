
from django.urls import path
from . import views


urlpatterns=[
    
     path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='con'),
    path('product/<int:pid>/', views.product_detail, name='product_detail'),
    path('product_gallery/<int:pid>/', views.product_gallery, name='gallery'),
    path('add_cart/<int:pid>/', views.add_cart, name='add_cart'),
    path('add_fav/<int:pid>/', views.add_fav, name='add_fav'),
    path('purchase/<int:pid>/', views.purchase, name='purchase'),
    
]