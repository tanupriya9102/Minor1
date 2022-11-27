from django.contrib import admin
from django.urls import path
from bertModel import views
urlpatterns = [
    path("",views.index,name='index'),
    path("index",views.index,name='index'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("form",views.form,name='form'),
    path("prediction",views.prediction,name='prediction'),
]
