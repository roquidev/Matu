from django.shortcuts import (render,
                              redirect,
                              get_object_or_404,
                              get_list_or_404)
from django.contrib import messages
from django.http import HttpResponse
import json
# External models import
from django.contrib.auth.models import User
# Local Models import
from .models import Profile, Agency, Tourist, Package
# ModelForms import
from .forms import AgencyForm, PackageForm


# Create your views here.

def demo(request):
    with open('data.json', 'r', encoding='utf-8') as file:
        list_packages = json.load(file)
    context = {
        'list_packages': list_packages
    }
    return render(
        request=request,
        template_name="demo/demo.html",
        context=context
    )


# ----------- Agency CRUD ----------- #

def list_agency(request):
    if request.user.is_authenticated:
        # Falta contemplar cuando el id es None
        user_authenticated_id = request.user.id
        # if request.user.id is not None else None
        agencies = get_list_or_404(Agency, profile=user_authenticated_id)
        context = {
            "agencies": agencies,
        }
        return render(
            request=request,
            template_name='demo/crud/agency/list_agency.html',
            context=context
        )
    else:
        return redirect("account_login")


def view_agency(request, id):
    if request.user.is_authenticated:
        # agency = Agency.objects.get(id=id)
        agency = get_object_or_404(Agency, id=id)
        context = {
            'agency': agency,
        }
        return render(
            request=request,
            template_name='demo/crud/agency/agency_detail.html',
            context=context
        )
    else:
        return redirect("account_login")


def edit_agency(request, id):
    if request.user.is_authenticated:
        # agency = Agency.objects.get(id=id)
        agency = get_object_or_404(Agency, id=id)
        if request.method == "GET":
            agency_edit_form = AgencyForm(instance=agency)
            context = {
                'agency_edit_form': agency_edit_form,
                'id': id
            }
            return render(
                request=request,
                template_name='demo/crud/agency/edit_agency.html',
                context=context
            )
        elif request.method == 'POST':
            agency_edit_form = AgencyForm(request.POST, instance=agency)
            if agency_edit_form.is_valid():
                agency_edit_form.save()
                # Message de django
                messages.success(
                    request=request,
                    message=f'Agencia {agency.name } actualizada.')
                context = {
                    'agency_edit_form': agency_edit_form,
                    'id': id
                }
                return render(
                    request=request,
                    template_name='demo/crud/agency/edit_agency.html',
                    context=context
                )
    else:
        return redirect("account_login")


def register_agency(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # Crear una instancia del formulario con los datos de la solicitud y el usuario autenticado
            agency_form = AgencyForm(request.POST, request.FILES)
            if agency_form.is_valid():
                # Obtener el Profile asociado al usuario autenticado
                # user_profile = Profile.objects.get(user=request.user)
                # Forma correcta preveendo si existe algun error
                user_profile = get_object_or_404(Profile, user=request.user)  # noqa: E501
                # Asignar el Profile al campo user en el formulario antes de guardar
                agency_instance = agency_form.save(commit=False)
                agency_instance.profile = user_profile
                agency_instance.save()
                return redirect("list_agency")
        else:
            # Si no es un método POST, simplemente instancía el formulario
            agency_form = AgencyForm()

        context = {
            'agency_form': agency_form,
        }
        return render(
            request=request,
            template_name='demo/crud/agency/register_agency.html',
            context=context
        )
    else:
        return redirect("account_login")


def confirm_delete_agency(request, id):
    agency = get_object_or_404(Agency, id=id)
    if request.method == "POST":
        agency.delete()
        return redirect("list_agency")
    context = {
        'agency': agency,
        'id': id
    }
    return render(
        request=request,
        template_name='demo/crud/agency/confirm_delete_agency.html',
        context=context
    )

# ----------- End of Agency CRUD ----------- #


# ----------- UserProfile CRUD ------------- #
# def view_tourist(request):
#     if request.user.is_authenticated:
#         # con -1 te trae el usuario actual
#         # Falta contemplar cuando el id es None
#         user_authenticated_id = request.user.id - 1  # if request.user.id is not None else None
#         # agencies = Agency.objects.filter(user_id=user_authenticated_id).all()
#         agencies = get_list_or_404(Tour, user_id=user_authenticated_id)
#         context = {
#             "agencies": agencies,
#         }
#         return render(
#             request=request,
#             template_name='demo/crud/agency/list_agency.html',
#             context=context
#         )
#     else:
#         return redirect("account_login")


def view_profile(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    if user_profile.user_type == "tourist":
        tourist = get_object_or_404(Tourist, profile=user_profile)
        context = {
            "tourist": tourist,
            "logo_url": tourist.image.url
        }
        return render(
            request=request,
            template_name='demo/crud/tourist/view_tourist.html',
            context=context
        )
    if user_profile.user_type == "tourism_agency":
        agency = get_object_or_404(Agency, id=user_profile.id)
        context = {
            'agency': agency,
            "logo_url": agency.banner_image.url
        }
        return render(
            request=request,
            template_name='demo/crud/agency/agency_detail.html',
            context=context
        )
    else:
        return HttpResponse("Ninguna coincidencia")

# ----------- End of Agency CRUD ----------- #


# ----------- Package CRUDX ----------- #
def list_package(request, id):
    if request.user.is_authenticated:
        # user_profile = get_object_or_404(Profile, user=request.user)
        agency = get_object_or_404(Agency, id=id)
        packages = get_list_or_404(Package, agency=agency)
        context = {
            'packages': packages,
            'agency': agency,
        }

        return render(
            request=request,
            template_name="demo/crud/package/list_package.html",
            context=context
        )
    else:
        return redirect('account_login')


def add_package(request, id):
    # Revisar el id de la agencia
    agency = get_object_or_404(Agency, id=id)
    # return HttpResponse(agency.agency_packages.get(id=id))
    if request.user.is_authenticated:
        if request.method == 'POST':
            # Crear una instancia del formulario con los datos de la solicitud
            package_form = PackageForm(request.POST, request.FILES)
            if package_form.is_valid():
                # Asignar la agencia al paquete antes de guardarlo
                package = package_form.save(commit=False)
                package.agency = agency
                package.save()
                return redirect("list_agency")
        else:
            # Si no es un método POST, simplemente instancía el formulario
            package_form = PackageForm()

        context = {
            # 'package': package,
            'package_form': package_form,
            'agency': agency,
        }
        return render(
            request=request,
            template_name='demo/crud/package/add_package.html',
            context=context
        )
    else:
        return redirect("account_login")


def view_package(request, id):
    package = get_object_or_404(Package, id=id)
    total_number_people = package.children + package.adults
    final_price = package.price_woth_discount
    context = {
        'package': package,
        'agency': package.agency,
        'total_number_people': total_number_people,
        'final_price': final_price,
    }
    return render(
        request=request,
        template_name="demo/crud/package/package_detail.html",
        context=context
    )


def edit_package(request, id):
    if request.user.is_authenticated:
        package = get_object_or_404(Package, id=id)
        if request.method == 'GET':
            package_edit_form = PackageForm(instance=package)
            context = {
                'package_edit_form': package_edit_form,
                'id': id,
                'agency': package.agency,
            }
            return render(
                request=request,
                template_name='demo/crud/package/edit_package.html',
                context=context
            )
        elif request.method == 'POST':
            package_edit_form = PackageForm(request.POST, instance=package)
            # Validacion de formulario
            if package_edit_form.is_valid():
                package_edit_form.save()
                # Dajango messages manager
                messages.success(
                    request=request,
                    message=f'Package {package.package_name } updated succesfully!'  # noqa: E501
                )
                context = {
                    'package_edit_form': package_edit_form,
                    'package': package,
                    'id': id,
                    'agency': package.agency,
                }

                return render(
                    request=request,
                    template_name='demo/crud/package/edit_package.html',
                    context=context
                )
    else:
        return redirect('account_login')


def confirm_delete_package(request, id):
    package = get_object_or_404(Package, id=id)
    if request.method == "POST":
        package_id = package.agency.id
        package.delete()
        return redirect("list_package", id=package_id)
    context = {
        'package': package,
        'id': id,
        'agency': package.agency,

    }
    return render(
        request=request,
        template_name='demo/crud/package/confirm_delete_package.html',
        context=context
    )

# ----------- End of Package CRUD ----------- #
