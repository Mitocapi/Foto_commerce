from django.urls import path
from . import views

app_name = "APPfoto"

urlpatterns = [
    path("", views.home, name="home"),
    path("firsthome/", views.first_home_view, name="first_home"),
    path("ricerca/", views.search, name="cercaFoto"),
    path("ricerca/<str:sstring>/<str:where>", views.FotoRicercaView.as_view(), name="ricerca_risultati"),

]