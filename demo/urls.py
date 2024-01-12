# External modules
from django.urls import path

# Local modules
from .views import demo, list_agency, register_agency, update_agency, delete_agency   # noqa: E501

urlpatterns = [
     path("demo/", demo, name="demo"),
     path('demo/list_agency/', view=list_agency, name="list_agency"),
     path('demo/register_agency/', view=register_agency, name="register_agency"),  # noqa: E501
     path('demo/update_agency/', view=update_agency, name="update_agency"),  # noqa: E501
     path('demo/delete_agency/', view=delete_agency, name="delete_agency"),  # noqa: E501
]
