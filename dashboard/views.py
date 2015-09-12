from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.utils import timezone

from .forms import PostForm
from models import Settings, Menu, Sidebar
from blog.models import Post

def index(request):
	menu_items = Menu.objects.order_by('position')
	sidebar_items = Sidebar.objects.order_by('position')
	context = {'menu_items' : menu_items, 'sidebar_items' : sidebar_items}
	return render(request, 'dashboard/index.html', context)

def settings(request):
	menu_items = Menu.objects.order_by('position')
	sidebar_items = Sidebar.objects.order_by('position')
	context = {'menu_items' : menu_items, 'sidebar_items' : sidebar_items}
	return render(request, 'dashboard/settings.html', context)

def post(request):
	post_list = Post.objects.order_by('-created_date')
	menu_items = Menu.objects.order_by('position')
	sidebar_items = Sidebar.objects.order_by('position')
	context = {'menu_items' : menu_items, 'sidebar_items' : sidebar_items, 'post_list' : post_list}
	return render(request, 'dashboard/post.html', context)

def menu(request):
	menu_items = Menu.objects.order_by('position')
	sidebar_items = Sidebar.objects.order_by('position')
	context = {'menu_items' : menu_items, 'sidebar_items' : sidebar_items}
	return render(request, 'dashboard/menu.html', context)

def new_post(request):
	sidebar_items = Sidebar.objects.order_by('position')

	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.published_date = timezone.now()
			post.created_date = timezone.now()
			post.save()
	else:
		form = PostForm()

	context = {'sidebar_items' : sidebar_items, 'form' : form}
	return render(request, 'dashboard/new_post.html', context)

def edit_post(request, post_id):
	sidebar_items = Sidebar.objects.order_by('position')
	post = get_object_or_404(Post, pk = post_id)

	if request.method == "POST":
		form = PostForm(request.POST, instance = post)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.published_date = timezone.now()
			post.created_date = timezone.now()
			post.save()
	else:
		form = PostForm(instance = post)

	context = {'sidebar_items' : sidebar_items, 'form' : form}
	return render(request, 'dashboard/new_post.html', context)