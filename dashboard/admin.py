from django.contrib import admin
from .models import Settings, Menu, Sidebar

class MenuAdmin(admin.ModelAdmin):
	list_display = ('label', 'url', 'position')
	ordering = ['position']

class SidebarAdmin(admin.ModelAdmin):
	list_display = ('label', 'url', 'position')
	ordering = ['position']

admin.site.register(Settings)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Sidebar, SidebarAdmin)
