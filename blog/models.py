from django.db import models
from django.utils import timezone
from demo.models import Profile


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_posts")  # noqa: E501
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="blog/images")
    # date = models.DateField(default=timezone.now)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-timestamp']

    def __str__(self) -> str:
        return f"{self.title} - {self.profile.user}"
