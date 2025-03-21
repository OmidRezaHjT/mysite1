from django.contrib import admin
from website.models import contact , newsletter
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name' ,'email','created_date')
    list_filter =('email',)
    search_fields = ('name', 'message')
    pass

admin.site.register(contact,ContactAdmin)
admin.site.register(newsletter)
