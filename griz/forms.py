from django import forms
from .models import Dog

# class EntryForm(forms.ModelForm):
#     class Meta:
#         model = models.Entry
#         fields = [ 'dog', 'tags',  ]
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
