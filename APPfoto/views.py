from django.shortcuts import render, redirect
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse

# Create your views here.


def home_view(request):
    return render(request, template_name="APPfoto/home.html")


from .forms import SearchForm  # Import your form class

from django.shortcuts import render
from django.views import View


class SearchWrongColoursView(View):
    template_name = "APPfoto/search_wrong_colour.html"  # Replace with the actual template path

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    # If you want to handle POST requests as well
    def post(self, request, *args, **kwargs):
        # Your post logic here
        return render(request, self.template_name)



class FotoListView(ListView):
    titolo="Abbiamo trovato queste foto"
    model = Foto
    template_name = "APPfoto/lista_foto.html"


from django.contrib import messages


def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            sstring = form.cleaned_data.get("search_string")
            where = form.cleaned_data.get("search_where")
            print("SIAMO IN SEARCH PRIMA O DOPO WRONG?")
            return redirect("APPfoto:ricerca_risultati", sstring, where)

    else:
        form = SearchForm()

    return render(request, "APPfoto/search.html", {"form": form})


class FotoListaRicercataView(FotoListView):
    titolo = "risultati ricerca"

    def get_queryset(self):
        sstring = self.request.resolver_match.kwargs["sstring"]
        where = self.request.resolver_match.kwargs["where"]

        if where == "name":
            qq = self.model.objects.filter(name__icontains=sstring)
        elif where == "landscape":
            # Filter using a boolean condition
            qq = self.model.objects.filter(landscape=True)
        elif where == "main_colour":
            # Filter using elements from a list
            COLOUR_CHOICES_to_filter = ["Black","Dark Blue","Green", "Gray", "Light Blue", "Orange", "Pink",
                                        "Purple", "Red", "White", "Yellow"]
            qq = self.model.objects.filter(main_colour__in=sstring)

        else:
            qq = self.model.objects.filter(artist_name__icontains=sstring)
        if not qq:
            print("si va?")
            return
        print(qq)
        return qq


class CreateFotoView(CreateView):
    title = "Aggiungi la tua foto alla galleria"
    form_class = CreateFotoForm
    template_name = "APPfoto/create_entry.html"
    success_url = reverse_lazy("APPfoto:home")
