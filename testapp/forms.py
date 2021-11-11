from django import forms
from .models import Day,Number,Numbergen

class DayCreateForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = "__all__"

class NumberCreateForm(forms.ModelForm):
    class Meta:
        model = Number
        fields ="__all__"

class NumbergenCreateForm(forms.ModelForm):
    class Meta:
        model = Numbergen
        fields = "__all__"