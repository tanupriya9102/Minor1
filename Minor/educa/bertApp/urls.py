from django.contrib import admin
from django.urls import path
from bertApp import views
urlpatterns = [
    path("",views.index,name='index'),
    path("index",views.index,name='index'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact')
]