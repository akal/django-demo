from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self',
                               blank=True,
                               null=True)
    template_name = models.CharField(max_length=100)

    def __str__(self):
        return 'Page %d: %s' % (self.pk, self.title)

class Content(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=2000,
                            blank=True)
    creator = models.ForeignKey(User, 
                                blank=True)
    # page = models.ForeignKey(Page, 
    #                          blank=True)
    page = models.ManyToManyField(Page,
                                  through='ContentLink',
                                  blank=True,
                                  null=True)

    def __str__(self):
        return 'Content %d: %s' % (self.pk, self.name)

class ContentLink(models.Model):
    content = models.ForeignKey(Content)
    page = models.ForeignKey(Page)
    block_name = models.CharField(max_length=64)


class Url(models.Model):
    url = models.CharField(max_length=256)
    page = models.ForeignKey(Page)

    def __str__(self):
        return 'Url:%d %s:(%s)' % (self.pk, self.url, self.page)

