from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SearchForm(forms.Form):
    CHOICE_LIST = [
        ("name", "Cerca nome foto"),
        ("artist_name", "Cerca nome fotografo"),
        ("main_colour", "Cerca per colore principale"),
        ("Orientamento", "Cerca per orientamento")
    ]

    COLOUR_CHOICES = ["Black", "Dark Blue", "Green", "Gray", "Light Blue", "Orange", "Pink",
                      "Purple", "Red", "White", "Yellow"]


    helper = FormHelper()
    helper.form_id = 'search_crispy_form'
    helper.form_method = "POST"
    helper.add_input(Submit('submit', 'Cerca'))

    search_string = forms.CharField(label="Cerca qualcosa", max_length=100, min_length=1, required=True)
    search_where = forms.ChoiceField(label="Ricerca per: ", required=True, choices=CHOICE_LIST)

    def clean_search_string(self):
        search_where = self.cleaned_data.get('search_where')
        search_string = self.cleaned_data.get('search_string')

        if search_where == "main_colour" and search_string not in self.COLOUR_CHOICES:
            raise forms.ValidationError("Invalid color choice for main_colour.")
        elif search_where == "landscape":
            if search_string.lower() not in ['true', 'false']:
                raise forms.ValidationError("Invalid value for landscape (expected 'True' or 'False').")
        else:

            pass

        return search_string


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
