from django import forms
from artwork.models import SearchParam

class FilterForm(forms.ModelForm):
    class Meta:
        model = SearchParam
        fields = ['searchName', 'title', 'price', 'width', 'height', 'artist', 'year']

    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)

        self.fields['searchName'].widget.attrs['placeholder'] = 'Search name for later'
        self.fields['title'].widget.attrs['placeholder'] = 'Title begins...'
        self.fields['price'].widget.attrs['placeholder'] = 'Max price'
        self.fields['width'].widget.attrs['placeholder'] = 'Max width'
        self.fields['height'].widget.attrs['placeholder'] = 'Max height'
        self.fields['artist'].widget.attrs['placeholder'] = 'Artist begins...'
        self.fields['year'].widget.attrs['placeholder'] = 'Created'
