from django.db import models
from django.utils import timezone
from demo.models import UserProfile


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']

    def __str__(self) -> str:
        return f"{self.title} - {self.user.user}"
