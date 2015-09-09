from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from models import Post, Menu

def index(request):
	post_list = Post.objects.order_by('-published_date')
	menu_items = Menu.objects.order_by('position')
	context = {'post_list' : post_list, 'menu_items' : menu_items }
	return render(request, 'blog/index.html', context)

def post(request, post_id):
	post = get_object_or_404(Post, pk = post_id)
	menu_items = Menu.objects.order_by('position')
	context = {'post' : post, 'menu_items' : menu_items }
	return render(request, 'blog/post.html', context)

def category(request, category_id):
	return HttpResponse("You are looking at category %s." % category_id)

def admin(request):
	if request.user.is_authenticated():
		return render(request, 'blog/admin/admin.html')
	else:
		return redirect('/blog/admin/login')

def login(request):
	return HttpResponse("Login")