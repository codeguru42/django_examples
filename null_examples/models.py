from django.db import models


class Foo(models.Model):
    foo = models.FloatField(blank=True, null=True)


class Bar(models.Model):
    bar = models.PositiveSmallIntegerField(blank=True, null=True)
