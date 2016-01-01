from django import forms

class UpdateForm(forms.Form):
    CHOICES = (('01','a'),
               ('02','b'),
               ('03','c'),
               ('14','d'),)
    departments = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())
