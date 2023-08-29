from django.shortcuts import render, redirect
from .forms import *
from django.views.generic.list import ListView

# Create your views here.


def home(request):
    return render(request, template_name="APP/base.html")


def first_home_view(request):
    return render(request, template_name="APP/first_home.html")


class FotoListView(ListView):
    titolo="Abbiamo trovato queste foto"
    model = Foto
    template_name="APP/lista_foto.html"


def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            sstring = form.cleaned_data.get("search_string")
            where = form.cleaned_data.get("search_where")
            return redirect("APPfoto:ricerca_risultati", sstring, where)

    else:
        form = SearchForm()

    return render(request,template_name="APP/search.html",context={"form":form})


class FotoRicercaView(FotoListView):
    titolo = "risultati ricerca"
    def get_queryset(self):
        sstring = self.request.resolver_match.kwargs["sstring"]
        where = self.request.resolver_match.kwargs["where"]

        if "name" in where:
            qq = self.model.objects.filter(titolo__icontains=sstring)
        else:
            qq = self.model.objects.filter(autore__icontains=sstring)

        return qq
