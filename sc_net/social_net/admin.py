from django.contrib import admin
from .models import Announcement, Person

class AnnAdmin(admin.ModelAdmin):
    list_display = ['person', 'title', 'created_at']
    list_filter = ['person', 'created_at']

class PerAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'age']
    list_filter = ['username', 'age']

admin.site.register(Announcement, AnnAdmin)
admin.site.register(Person, PerAdmin)
