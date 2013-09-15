from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'minicms',
    url(r'(?P<path>.+)$', 'views.minicms')
)
