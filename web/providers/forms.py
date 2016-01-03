from django import forms

class UpdateForm(forms.Form):
    CHOICES = (('01','a'),
               ('02','b'),
               ('03','c'))
    departments = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())
