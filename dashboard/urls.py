from django.conf.urls import url
from . import views

urlpatterns = [
	# Ex: /dashboard/
    url(r'^$', views.index, name='index'),
    # Ex: /dashboard/settings
    url(r'^settings/$', views.settings, name="settings"),
    # Ex: /dashboard/post
    url(r'^post/$', views.post, name="post"),
    # Ex: /dashboard/post/new
    url(r'^post/new/$', views.new_post, name="new_post"),
    # Ex: /dashboard/post/edit/5
    url(r'^post/edit/(?P<post_id>[0-9]+)/$', views.edit_post, name='edit_post'),
    # Ex: /dashboard/post/delete/5
    url(r'^post/delete/(?P<post_id>[0-9]+)/$', views.delete_post, name='delete_post'),
    # Ex: /dashboard/menu
    url(r'^menu/$', views.menu, name="menu"),
    # Ex: /dashboard/categories
    url(r'^categories/$', views.category, name="category"),
]