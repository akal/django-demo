from contactform.forms import ContactRequestForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

def form(request):
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contact_saved'))
    else:
        form = ContactRequestForm()
    return render(request, 'contact_form.html', {
            'contact_form': form})
        
def contact_saved(request):
    return render(request, 'contact_saved.html')
