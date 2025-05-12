from django.urls import path
from .views import (
    PostListView,
    LostPostListView,
    FoundPostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/add/", PostCreateView.as_view(), name="post_form"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("lost/", LostPostListView.as_view(), name="lost_post_list"),
    path("found/", FoundPostListView.as_view(), name="found_post_list"),
]
