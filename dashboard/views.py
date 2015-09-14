from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.utils import timezone

from .forms import PostForm, SettingsForm
from models import Settings, Sidebar
from blog.models import Post

def index(request):
	sidebar_items = Sidebar.objects.order_by('position')
	context = {'sidebar_items' : sidebar_items}
	return render(request, 'dashboard/index.html', context)

def settings(request):
	sidebar_items = Sidebar.objects.order_by('position')
	settings = get_object_or_404(Settings, pk = 1)
	if request.method == "POST":
		form = SettingsForm(request.POST, instance = settings)
		if form.is_valid():
			settings = form.save(commit = False)
			settings.save()
			return HttpResponseRedirect('/dashboard/settings')
	else:
		form = SettingsForm(instance = settings)

	context = {'sidebar_items' : sidebar_items, 'form' : form}
	return render(request, 'dashboard/settings.html', context)

def post(request):
	post_list = Post.objects.order_by('-created_date')
	sidebar_items = Sidebar.objects.order_by('position')
	context = {'sidebar_items' : sidebar_items, 'post_list' : post_list}
	return render(request, 'dashboard/post.html', context)

def menu(request):
	sidebar_items = Sidebar.objects.order_by('position')
	context = {'sidebar_items' : sidebar_items}
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
			return HttpResponseRedirect('/dashboard/post')
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
			return HttpResponseRedirect('/dashboard/post')
	else:
		form = PostForm(instance = post)

	context = {'sidebar_items' : sidebar_items, 'form' : form}
	return render(request, 'dashboard/edit_post.html', context)

def delete_post(request, post_id):
	post = get_object_or_404(Post, pk = post_id)
	post.delete()
	return HttpResponseRedirect('/dashboard/post')


def category(request):
	sidebar_items = Sidebar.objects.order_by('position')
	context = {'sidebar_items' : sidebar_items}
	return render(request, 'dashboard/category.html', context)