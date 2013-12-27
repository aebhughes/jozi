from django.shortcuts import render, get_object_or_404
from blog.models import Post  
import datetime

def index(request, ):
	# get the blog posts that are published
	cdate = datetime.date.today() - datetime.timedelta(days=1)
	posts = Post.objects.filter(published = True, exDate__gt= cdate).order_by('exDate')
	# now return the rendered template
	return render(request, 'blog/index.html', {'posts':posts})

def post(request, slug):
	# get the Post object
	post = get_object_or_404(Post, slug=slug)
	# now return the rendered template
	return render(request, 'blog/post.html', {'post':post})

def mobile_index(request, ):
	# get the blog posts that are published
	cdate = datetime.date.today() - datetime.timedelta(days=1)
	posts = Post.objects.filter(published = True, exDate__gt= cdate).order_by('exDate')
	# now return the rendered template
	return render(request, '/mobile/', {'posts':posts})

def mobile_post(request, slug):
	# get the Post object
	post = get_object_or_404(Post, slug=slug)
	# now return the rendered template
	return render(request, 'blog/mobile_post.html', {'post':post})

