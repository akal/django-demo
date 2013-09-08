from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self',
                               blank=True)
    template_name = models.CharField(max_length=100)

class Content(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=2000,
                            blank=True)
    creator = models.ForeignKey(User, 
                                blank=True)
    page = models.ForeignKey(Page, 
                             blank=True)
