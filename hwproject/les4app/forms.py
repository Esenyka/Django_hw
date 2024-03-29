import datetime

from django import forms


class UserFrom(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)


class ManyFieldFrom(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)
    height = forms.FloatField()
    is_active = forms.BooleanField(required=False)
    birthday = forms.DateField(initial=datetime.date.today)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])


class ManyFieldFormsWidget(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'user@mail.ru'}))
    age = forms.IntegerField(min_value=0, max_value=120, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    birthday = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control',
                                                                                          'type': 'date'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')],
                               widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))