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






# Create your models here.
# class UserDetails(models.Model):
#     USER_TYPE_CHOICES = [
#         ('tourist', 'Tourist'),
#         ('tourism_agency', 'Tourism Agency'),
#     ]
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     userId = models.AutoField(primary_key=True)
#     countryUser = CountryField(blank_label="(select country)")
#     userType = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

#     def __str__(self) -> str:
#         return f"{ self.userId } - { self.user.username } - { self.userType.replace('_', ' ').capitalize() }"  # noqa: E501


# class Agency(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     agencyId = models.AutoField(primary_key=True)
#     agencyName = models.CharField(max_length=100)
#     agencyDescription = models.TextField(blank=True, null=True, help_text="Tell us about your agency...")  # noqa: E501
#     # phoneNumber = PhoneNumberField(region='PE', null=False, blank=False)


# class TravelPackage(models.Model):
#     packageId = models.AutoField(primary_key=True)
#     packageName = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True, help_text="Add a aditional description...")  # noqa: E501
#     duration = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     startDate = models.DateField(default=timezone.now)
#     endDate = models.DateField()
#     availableSlots = models.PositiveIntegerField()
#     comments = models.TextField(blank=True, null=True, help_text="Comment us about your experience...")  # noqa: E501
#     SCORE_CHOICES = [
#         ('1.0', '1 star'),
#         ('2.0', '2 stars'),
#         ('3.0', '3 stars'),
#         ('4.0', '4 stars'),
#         ('5.0', '5 stars'),
#     ]
#     score = models.CharField(max_length=3, choices=SCORE_CHOICES, null=True)
#     agencyId = models.ForeignKey(Agency, on_delete=models.CASCADE)

