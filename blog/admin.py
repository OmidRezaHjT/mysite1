from django.contrib import admin
from blog.models import post , category
from django_summernote.admin import SummernoteModelAdmin
from blog.models import post

class postAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','author' ,'counted_views','status','publish_date','created_date')
    list_filter = ('status','author')
    search_fields = ['title','content']
    summernote_fields = ('content',)
admin.site.register(post,postAdmin)  
admin.site.register(category)