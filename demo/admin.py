from django.contrib import admin
from .models import Profile, Tourist, Agency, Package, Group
# Register your models here.


admin.site.register([
    Profile,
    Tourist,
    Agency,
    Package,
    Group
])
