from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact_info, name="ContactUs"),
    path("tracker/", views.tracker, name="TrakingStatus"),
    path("search/", views.search, name="Search"),
    path("productview/<int:myid>", views.prodView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),

]