from django.urls import path
from . import views

urlpatterns = [

    path('home/', views.home, name='home'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('product_list/', views.product_list, name='product_list'),
    path('userproductlist/',views.userproductlist,name='userproductlist'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:id>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:id>/', views.delete_product, name='delete_product'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/',views.cart, name='cart'),
    path('delete_cart/<int:id>/', views.delete_cart, name='delete_cart'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('add_to_wishlist/<int:id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('thank_you/', views.thank_you, name='thank_you'),

]