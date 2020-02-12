from django import forms
from django.forms import ModelForm
from .models import ToDo_obj

class DateInput(forms.DateInput):
    input_type = 'date'

class ToDo_objCreateForm(ModelForm):

    class Meta:
        model = ToDo_obj
        fields = ('title', 'explaination', 'deadline', )
        widgets = {
            'deadline': DateInput(),
        }

class ToDo_objUpdateForm(ModelForm):

    class Meta:
        model = ToDo_obj
        fields = ('title', 'explaination', 'deadline', 'status')