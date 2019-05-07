from django import forms

from null_examples import models


class FooForm(forms.ModelForm):
    class Meta:
        model = models.Foo
        fields = '__all__'


class BarForm(forms.ModelForm):
    class Meta:
        model = models.Bar
        fields = '__all__'
