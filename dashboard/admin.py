from django.contrib import admin
from .models import Settings, Sidebar

class SidebarAdmin(admin.ModelAdmin):
	list_display = ('label', 'url', 'position')
	ordering = ['position']

class SettingsAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'description')

admin.site.register(Settings, SettingsAdmin)
admin.site.register(Sidebar, SidebarAdmin)
