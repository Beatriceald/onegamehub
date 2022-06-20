from django.contrib import admin
from .models import Urls

class urlsAdmin(admin.ModelAdmin):
    list_display = ('id', 'url_slug')
    list_display_links = ('id', 'url_slug')

admin.site.register(Urls, urlsAdmin)
# Register your models here.
