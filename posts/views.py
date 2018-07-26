from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def post_create(request):
	context = {
		"title": "create a post"
	}
	return render(request, "posts/post_create.html", context)

def post_update(request):
	context = {
		"update": "update"
	}
	return render(request, "posts/post_create.html", context)

def post_delete(request):
	context = {
		"delete": "delete"
	}
	return render(request, "posts/post_create.html", context)

def post_detail(request):
	context = {}
	return render(request, "posts/post_create.html", context)

def post_list(request):
	queryset = Post.objects.all()
	context = {
		"queryset_list": queryset,
	}
	return render(request, "posts/post_create.html", context)


