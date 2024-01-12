from django.contrib import admin
from .models import UserProfile, Tourist, Agency, TravelPackage
# Register your models here.


admin.site.register([
    UserProfile,
    Tourist,
    Agency,
    TravelPackage
])
