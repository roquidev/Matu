from django.db import models

# from django.contrib.auth.models import User
# from django_countries.fields import CountryField
# from django.utils import timezone
# from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # noqa: 501
    image = models.ImageField(default='users/image_user.png', upload_to='users/')  # noqa: 501
    location = models.CharField(max_length=80, null=True, blank=True)
    bio = models.TextField(max_length=400, null=True, blank=True)
