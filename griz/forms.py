from django import forms
from .models import Dog, Entry



class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [ 'dog', 'tags', 'date' ]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
#
# class EntryFilterForm(forms.Form):
#     dog = forms.ModelChoiceField(
#         queryset=Dog.objects.all(),
#         required=False,
#         empty_label="All Dogs"
#     )
#     tags = forms.ModelMultipleChoiceField(
#         queryset=Tag.objects.all(),
#         required=False,
#         widget=forms.CheckboxSelectMultiple
#     )
