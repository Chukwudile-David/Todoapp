from attr import field
from django import forms
from .models import Mytodo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Mytodo
        fields =['task']

    #C:\Users\wesley uvci\Desktop\pythonProject1\Todos\Todoapp
