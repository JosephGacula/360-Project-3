from django.db import models
from django.urls import reverse
from django.conf import settings


class Post(models.Model):
    CATEGORY_CHOICES = [
        ("LOST", "Lost"),
        ("FOUND", "Found"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"pk": self.pk})
