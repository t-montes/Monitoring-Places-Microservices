from django import forms
from django.conf import settings
import requests

def get_variables():
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    variables = r.json()
    Var_Choices = []
    for variable in variables:
        Var_Choices.append([variable["id"], variable["name"]])
    return Var_Choices

class MeasurementForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(MeasurementForm, self).__init__(*args, **kwargs)
        self.fields['variable'] = forms.ChoiceField(
            choices=get_variables() )

    value = forms.FloatField()
    unit = forms.CharField(max_length=20)
    place = forms.CharField(max_length=30)