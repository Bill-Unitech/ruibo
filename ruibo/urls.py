"""ruibo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from mainpage import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^show_cars_1/$', views.show_cars_1),
    url(r'^show_cars_2/$', views.show_cars_2),
    url(r'^show_cars_3/$', views.show_cars_3),
    url(r'^show_cars_4/$', views.show_cars_4),
    url(r'^show_cars_5/$', views.show_cars_5),
    url(r'^show_cars_6/$', views.show_cars_6),
    url(r'^show_cars_7/$', views.show_cars_7),
    url(r'^show_cars_8/$', views.show_cars_8),
    url(r'^show_cars_9/$', views.show_cars_9),
    url(r'^show_cars_10/$', views.show_cars_10),
    url(r'^show_cars_11/$', views.show_cars_11),
    url(r'^show_cars_12/$', views.show_cars_12),
    url(r'^contact/$', views.contact_page),

]
