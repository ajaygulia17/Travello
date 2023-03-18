from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="home"),
	path('destination', views.destinations, name="destination"),
    path('about', views.about, name="about"),
    path('news', views.news, name="news"),
    path('contact', views.contact, name="contact"),
    path('package', views.package, name="package"),
    path('addpackage', views.addpackage, name="addpackage"),
]