from django.contrib import admin

from.models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ('address','string_name')

admin.site.register(Link, LinkAdmin)