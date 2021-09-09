from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),


    path("fashion", views.fashion, name="fashion"),
    path("beauty", views.beauty, name="beauty"),
    path("accesories", views.accesories, name="accesories"),

    # path("home/", views.home, name="home"),
    path("store/<str:id>/", views.store, name="store"),
    path("review/", views.review, name="review"),
    path("cart", views.cart, name="cart"),

    path("checkout", views.checkout, name="checkout"),
    path("update_item/", views.updateItem, name="update_item"),

    path("process_order/", views.processOrder, name="process_order"),
]