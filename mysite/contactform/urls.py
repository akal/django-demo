from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'contactform',
    url(r'form/$', 'views.form', name='contactform'),
    url(r'contact_saved/$', 'views.contact_saved', name='contact_saved')
)
