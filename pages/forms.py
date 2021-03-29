from django import forms
from artwork.models import SearchParam

class FilterForm(forms.Form):
    title = forms.CharField(max_length=120)
    price = forms.DecimalField(decimal_places=2, max_digits=1000)
    width = forms.IntegerField()
    height = forms.IntegerField()
    artist = forms.CharField(max_length=120)
    user = forms.CharField()
    year = forms.IntegerField()
    sortBy = forms.CharField(max_length=10)
