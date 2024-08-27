from django import forms
# here use bootstrap 5.3
class Searchform(forms.Form):
    Search = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control w-50'})
    )