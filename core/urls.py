from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('store/', views.store, name = 'store'),
    # path('product/', views.product, name = 'product'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('search/', views.search, name = 'search'),
    path('sell/', views.sell, name = 'sell'),
    path('cart/', views.cart, name = 'cart'),
    path('product-detail/<int:pk>', views.ProductsDetailView.as_view(), name = 'product_detail'),
    path('add-cart/<int:pk>', views.add_to_cart, name = 'add-cart'),
    path('remove-cart/<int:item_id>', views.remove_from_cart, name = 'remove-cart'),
    path('subtract-cart/<int:pk>', views.subtract_from_cart, name = 'subtract'),
    path('increase/<int:pk>/', views.increase_cart_quantity, name = 'increase'),
    
]