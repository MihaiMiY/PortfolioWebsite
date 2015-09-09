from django.contrib import admin
from .models import Post, Menu, Category, UserProfile

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author','created_date', 'published_date', 'category')
	search_fields = ['title']

class MenuAdmin(admin.ModelAdmin):
	list_display = ('label', 'url', 'position')
	ordering = ['position']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'url')


admin.site.register(Post, PostAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(UserProfile)