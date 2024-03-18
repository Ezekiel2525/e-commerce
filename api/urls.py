from django.urls import path
from . import views


urlpatterns = [
    path('api/products', views.products_list),
    path('api/product/<int:pk>/', views.product),
    path('api/product_view', views.product_view),
    path('api/each_product', views.each_product),
   
]