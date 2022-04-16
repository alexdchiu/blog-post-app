from django.urls import path

from posts.views import list_posts, create_post, post_detail

urlpatterns = [
  path("", list_posts, name="posts_list"),
  path("new/", create_post, name="create_post"),
  path("<int:id>/", post_detail, name="post_detail"),
]