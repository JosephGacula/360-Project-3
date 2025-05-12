from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]
    paginate_by = 12


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"


class LostPostListView(PostListView):
    """
    Displays only posts in the LOST category
    Inherits all functionality from PostListView
    """

    def get_queryset(self):
        # Get the base queryset and filter it
        return super().get_queryset().filter(category="LOST")


class FoundPostListView(PostListView):
    def get_queryset(self):
        return super().get_queryset().filter(category="FOUND")


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_form.html"

    # Only allow author to edit
    def test_func(self):
        return self.request.user == self.get_object().author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "posts/post_confirm_delete.html"
    success_url = reverse_lazy("posts:post_list")

    # Only allow author to delete
    def test_func(self):
        return self.request.user == self.get_object().author
