import os
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
# from languages.fields import LanguageField


# Extension del modelos User
class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('tourist', 'Tourist'),
        ('tourism_agency', 'Tourism Agency'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')  # noqa: E501
    user_type = models.CharField(max_length=200, choices=USER_TYPE_CHOICES)
    country = CountryField(blank_label="Select country")
    # language = LanguageField(max_length=100)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self) -> str:
        return f"{ self.user.username } - { self.user_type.replace('_', ' ').capitalize() }"  # noqa: E501


def get_tourist_image_path(instance, filename):
    # Genera la ruta dinámica user/nombre_del_usuario/nombre_de_la_imagen
    return os.path.join('users', instance.profile.user.username, filename)


def get_agency_image_path(instance, filename):
    return os.path.join('agencies', instance.profile.user.username, filename)


# Turistas
class Tourist(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="profile_tourist")  # noqa: E501
    bio = models.TextField(default="This is my biography...", max_length=1500)
    image = models.ImageField(default='users/logo_default.png', upload_to=get_tourist_image_path)  # noqa: 501

    class Meta:
        verbose_name = 'Tourist'
        verbose_name_plural = 'Tourists'

    def __str__(self) -> str:
        return f"{ self.profile.user.username }"  # noqa: E501


class Agency(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_agencies")  # noqa: E501
    name = models.CharField(unique=True, blank=False, null=False, max_length=100)  # noqa: E501
    banner_image = models.ImageField(default='agencies/banner_default.png', upload_to=get_agency_image_path)  # noqa: 501
    description = models.TextField(blank=True, null=True, help_text="Tell us about your agency...")  # noqa: E501
    # Investigar más acerca del valor default
    phone_number = PhoneNumberField(region='PE', default='+51', null=False, blank=False)  # noqa: E501

    class Meta:
        verbose_name = 'Agency'
        verbose_name_plural = 'Agencies'
        ordering = ['id']

    def __str__(self) -> str:
        return f"{self.name} - {self.profile.user}"


class Package(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name="agency_packages")  # noqa: E501
    package_name = models.CharField(unique=True, max_length=100)
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

    def price_woth_discount(self):
        final_price = self.base_price - (self.base_price * (self.discount / 100))  # noqa: E501
        return final_price

    def __str__(self) -> str:
        return self.package_name


class Group(models.Model):
    tourists = models.ManyToManyField(Tourist)
    title = models.TextField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Travel Group"
        verbose_name_plural = "Travel Groups"
        ordering = ["-created_at"]
