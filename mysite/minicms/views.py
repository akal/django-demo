from minicms.models import Url, Page, Content
from django.shortcuts import render

def minicms(request, path):
    print 'path: ', path
    # get matching url
    if path.endswith('/'):
        path = path[:-1]
    url = Url.objects.get(url=path)
    # get contents mapping to page defined by url
    page = url.page
    title = page.title
    template = page.template_name
    contents = dict([(l.block_name, l.content.text) 
                     for l in page.contentlink_set.all()])
    contents['page_title'] = title
    
    return render(request, template, contents)
