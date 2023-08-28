from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *

class SearchForm(forms.Form):
    CHOICE_LIST = [("Foto","Cerca nome foto"), ("Fotografo", "Cerca nome fotografo"),
                   ("Colore", "Cerca per colore principale"), ("Orientamento", "Cerca per orientamento")]

    search_string = forms.CharField(label="Search String", max_length=100, min_length=1, required=True)
    search_where = forms.ChoiceField(label="Search Where?", required=True, choiches=CHOICE_LIST)


class FotoCrispyForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_id = 'foto-crispy-form'
    helper.form_method = 'POST'
    helper.add_input(Submit('submit','Submit'))

    class Meta:
        model = Foto
        fields = ('name', 'artist_name', 'main_colour', 'landscape')
