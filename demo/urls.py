# External modules
from django.urls import path
# Local modules
from .views import (demo, view_agency, register_agency,
                    edit_agency,
                    list_agency,
                    confirm_delete_agency,
                    view_profile,
                    list_package,
                    add_package,
                    view_package,
                    edit_package,
                    confirm_delete_package
                    # view_tourist,
                    )   # noqa: E501

urlpatterns = [
     path("demo/", demo, name="demo"),
     # Agency CRUD
     path('demo/list_agency/', view=list_agency, name="list_agency"),  # noqa: E501
     path('demo/register_agency/', view=register_agency, name="register_agency"),  # noqa: E501
     path('demo/view_agency/<int:id>', view=view_agency, name="view_agency"),
     path('demo/edit_agency/<int:id>', view=edit_agency, name="edit_agency"),  # noqa: E501
     path('demo/confirm_delete_agency/<int:id>/', view=confirm_delete_agency, name="confirm_delete_agency"),  # noqa: E501
     # Profile CRUD
     path('demo/view_profile/', view=view_profile, name="view_profile"),  # noqa: E501
     # Package CRUD
     path('demo/list_package/<int:id>', view=list_package, name="list_package"),  # noqa: E501
     path('demo/add_package/<int:id>', view=add_package, name="add_package"),  # noqa: E501
     path('demo/view_package/<int:id>', view=view_package, name="view_package"),
     path('demo/edit_package/<int:id>', view=edit_package, name="edit_package"),
     path('demo/confirm_delete_package/<int:id>/', view=confirm_delete_package, name="confirm_delete_package"),  # noqa: E501
     # path('demo/view_tourist/<int:id>/', view=view_tourist, name="view_tourist"),  # noqa: E501
]
