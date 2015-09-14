from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.index, name = "index"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace = "blog")),
    url(r'^dashboard/', include('dashboard.urls', namespace = "dashboard")),
]
