from django import forms
from .models import Todo
from django.contrib.auth.models import User

class AddTodo(forms.ModelForm):
    # user = forms.ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = Todo
        fields = ('title',)