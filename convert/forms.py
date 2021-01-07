from django import forms


class InputForm(forms.Form):

  Datos=forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 15}))
