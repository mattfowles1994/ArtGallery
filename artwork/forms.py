from django import forms

from .models import Artwork

class ArtworkForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Artwork
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "CFE" in title:
            raise forms.ValidationError('Not a valid title')
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('edu'):
            raise forms.ValidationError('not a valid email')
        return email

class RawArtForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()