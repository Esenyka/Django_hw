from django import forms


class ImageForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
