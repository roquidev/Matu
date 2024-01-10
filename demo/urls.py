# External modules
from django.urls import path

# Local modules
from .views import demo

urlpatterns = [
     path("demo/", demo, name="demo"),
]
