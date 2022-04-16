from django.shortcuts import render, redirect

# Create your views here.
from posts.models import Post
from posts.forms import PostForm

def list_posts (request):
  posts = Post.objects.all()
  context = {
    "posts": posts,
  }
  return render(request, "posts/main.html", context)

def create_post(request):
  form = PostForm()
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("posts_list")
  context = {
    "form": form,
  }
  return render(request, "posts/create.html", context)

def post_detail(request, id):
  post = Post.objects.get(id=id)
  context = {
    "post": post
  }
  return render (request, "posts/detail.html", context)