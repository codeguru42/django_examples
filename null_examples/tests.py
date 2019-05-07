from django.test import TestCase

from null_examples import models, forms


class ModelTests(TestCase):
    def testFooNull(self):
        foo = models.Foo.objects.create(foo='')

    def testBarNull(self):
        bar = models.Bar.objects.create(bar='')


class FormTests(TestCase):
    def testFooNull(self):
        form = forms.FooForm(data={'foo': ''})
        form.is_valid()
        form.save()

    def testBarNull(self):
        form = forms.BarForm(data={'bar': ''})
        form.is_valid()
        form.save()
