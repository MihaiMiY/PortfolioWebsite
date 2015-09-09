from django.conf.urls import url
from . import views

urlpatterns = [
	# Ex: /blog/
    url(r'^$', views.index, name='index'),
    # Ex: /blog/post/5/
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post, name='post'),
    # Ex: /blog/category/
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name="category"),
    # Ex: /blog/admin
    url(r'^admin/$', views.admin, name="admin"),
    # Ex: /blog/admin/login
    url(r'^admin/login/$', views.login, name="login")
    # Ex: /blog/admin/register
]