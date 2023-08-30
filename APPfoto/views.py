from django.shortcuts import render, redirect
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.


def home_view(request):
    return render(request, template_name="APPfoto/home.html")


class FotoListView(ListView):
    titolo="Abbiamo trovato queste foto"
    model = Foto
    template_name= "APPfoto/lista_foto.html"


def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            sstring = form.cleaned_data.get("search_string")
            where = form.cleaned_data.get("search_where")
            return redirect("APPfoto:ricerca_risultati", sstring, where)

    else:
        form = SearchForm()

    return render(request, template_name="APPfoto/search.html", context={"form":form})


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


class CreateFotoView(CreateView):
    title = "Aggiungi la tua foto alla galleria"
    form_class = CreateFotoForm
    template_name = "APPfoto/create_entry.html"
    success_url = reverse_lazy("APPfoto:home")
