from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def home_view(request):
    return render(request, template_name="APPfoto/home.html")


from .forms import SearchForm  # Import your form class

from django.shortcuts import render
from django.views import View




class SearchWrongColourView(View):
    template_name = "APPfoto/search_wrong_colour.html"

    def get(self, request, *args, **kwargs):
        form = SearchForm()  # Replace with your actual form class
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        if request.method == "POST":
            form = SearchForm(request.POST)
            if form.is_valid():
                sstring = form.cleaned_data.get("search_string")
                where = form.cleaned_data.get("search_where")
                return redirect("APPfoto:ricerca_risultati", sstring, where)
            else:
                context = {'form': form}
            return render(request, self.template_name, context)


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
            return redirect("APPfoto:ricerca_risultati", sstring, where)

    else:
        form = SearchForm()

    return render(request, "APPfoto/search.html",context= {"form": form})


class FotoListaRicercataView(FotoListView):
    titolo = "risultati ricerca"

    def get_queryset(self):
        sstring = self.kwargs['sstring']
        where = self.kwargs['where']


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

        return qq


class CreateFotoView(CreateView):
    title = "Aggiungi la tua foto alla galleria"
    form_class = CreateFotoForm
    template_name = "APPfoto/create_entry.html"
    success_url = reverse_lazy("APPfoto:home")


@login_required
def my_situation(request):
     user = get_object_or_404(User, pk=request.user.pk)
     return render(request,"APPfoto/situation.html")
