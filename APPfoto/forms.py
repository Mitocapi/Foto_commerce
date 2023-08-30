from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *

class SearchForm(forms.Form):
    CHOICE_LIST = [("name","Cerca nome foto"), ("artist_name", "Cerca nome fotografo"),
                   ("main_colour", "Cerca per colore principale"), ("Orientamento", "Cerca per orientamento")]

    helper = FormHelper()
    helper.form_id = 'search_crispy_form'
    helper.form_method = "POST"
    helper.add_input(Submit('submit', 'Cerca'))

    search_string = forms.CharField(label="Cerca qualcosa", max_length=100, min_length=1, required=True)
    search_where = forms.ChoiceField(label="Ricerca per: ", required=True, choices=CHOICE_LIST)


class FotoCrispyForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_id = 'foto-crispy-form'
    helper.form_method = 'POST'
    helper.add_input(Submit('submit','Submit'))

    class Meta:
        model = Foto
        fields = ('name', 'artist_name', 'main_colour', 'landscape')


class CreateFotoForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_id = "addfoto_crispy_form"
    helper.form_method = "POST"
    helper.add_input(Submit("submit", "Aggiungi Foto"))

    class Meta:
        model = Foto
        fields = ["name", "artist_name", "main_colour", "landscape","actual_photo"]
