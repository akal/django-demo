from django.contrib import admin
from minicms.models import Page, Content, Url, ContentLink

def myaction(modeladmin, request, queryset):
    print 'My Action: '
    for q in queryset: 
        print q
myaction.short_description = 'My Action'

class PageAdmin(admin.ModelAdmin):
    actions = [myaction]

admin.site.register(Page, PageAdmin)
admin.site.register(Content)
admin.site.register(ContentLink)
admin.site.register(Url)
