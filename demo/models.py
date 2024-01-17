from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
# Extension del modelos User
class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('tourist', 'Tourist'),
        ('tourism_agency', 'Tourism Agency'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')  # noqa: E501
    user_type = models.CharField(max_length=200, choices=USER_TYPE_CHOICES)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self) -> str:
        return f"{ self.user.username } - { self.user_type.replace('_', ' ').capitalize() }"  # noqa: E501


# Turistas
class Tourist(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='tourist_profile')  # noqa: E501
    bio = models.TextField(default="This is my biography...", max_length=1500)
    image = models.ImageField(default='users/image_user.png', upload_to='users/')  # noqa: 501
    countryUser = CountryField(blank_label="Select country")

    class Meta:
        verbose_name = 'Tourist'
        verbose_name_plural = 'Tourists'

    def __str__(self) -> str:
        return f"{ self.user_profile.user.username }"  # noqa: E501


class Agency(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(unique=True, blank=False, null=False, max_length=100)  # noqa: E501
    # banner_image = models.ImageField(default='users/image_user.png', upload_to='users/')  # noqa: 501
    description = models.TextField(blank=True, null=True, help_text="Tell us about your agency...")  # noqa: E501
    # Investigar más acerca del valor default
    phone_number = PhoneNumberField(region='PE', default='PE', null=False, blank=False)  # noqa: E501

    class Meta:
        verbose_name = 'Agency'
        verbose_name_plural = 'Agencies'
        ordering = ['id']

    def __str__(self) -> str:
        return f"{self.name} - {self.user.user}"


class TravelPackage(models.Model):
    packageName = models.CharField(unique=True, max_length=100)
    package_description = models.TextField(blank=True, null=True, help_text="Add a aditional description...")  # noqa: E501
    children = models.IntegerField(default=0)
    adults = models.IntegerField(default=1)
    check_in = models.DateTimeField(default=timezone.now)
    check_out = models.DateTimeField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    available_slots = models.PositiveIntegerField()
    comments = models.TextField(blank=True, null=True, help_text="Comment us about your experience...")  # noqa: E501
    SCORES_TO_CHOOSE = [
        (1, '1 start'),
        (2, '2 starts'),
        (3, '3 starts'),
        (4, '4 starts'),
        (5, '5 starts'),
    ]
    score = models.IntegerField(choices=SCORES_TO_CHOOSE, default=None, null=True)  # noqa: E501
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)

    def price_woth_discount(self):
        final_price = self.base_price - (self.base_price * (self.discount / 100))  # noqa: E501
        return final_price
