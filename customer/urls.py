from django.urls import path
from.import views

urlpatterns = [
    path('',views.home, name="homepage"),
    path('index', views.index, name="index"),
    path('base', views.base, name="base"),
    path('contact', views.contact, name="contact"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('types', views.types, name="types"),
    path('authors', views.authors, name="authors")

]