from django.conf.urls import url
from . import views

urlpatterns = [
	# ex: /blog/
    url(r'^$', views.index, name='index'),
    # ex: /blog/post/5/
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post, name='post'),
]