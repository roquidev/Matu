# External modules
from django.urls import path
# Local modules
from .views import (demo, view_agency, register_agency,
                    edit_agency,
                    list_agency, confirm_delete_agency,
                    )   # noqa: E501

urlpatterns = [
     path("demo/", demo, name="demo"),
     # Agency CRUD
     path('demo/list_agency/', view=list_agency, name="list_agency"),  # noqa: E501
     path('demo/register_agency/', view=register_agency, name="register_agency"),  # noqa: E501
     path('demo/view_agency/<int:id>', view=view_agency, name="view_agency"),
     path('demo/edit_agency/<int:id>', view=edit_agency, name="edit_agency"),  # noqa: E501
     path('demo/confirm_delete_agency/<int:id>/', view=confirm_delete_agency, name="confirm_delete_agency"),  # noqa: E501
]
