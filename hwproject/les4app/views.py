from django.shortcuts import render
import logging
from .forms import UserFrom, ManyFieldFrom, ManyFieldFormsWidget

logger = logging.getLogger(__name__)

# Create your views here.


def user_form(request):
    if request.method == 'POST':
        form = UserFrom(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']

            logger.info(f"Get {name=}, {email=}, {age=}")
    else:
        form = UserFrom()
    return render(request, 'les4app/user_form.html', {'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldFormsWidget(request.POST)
        if form.is_valid():
            logger.info(f"Get {form.changed_data=}")
    else:
        form = ManyFieldFormsWidget()
    return render(request, 'les4app/many_fields_form.html', {'form': form})


