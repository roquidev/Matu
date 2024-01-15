from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.http import HttpResponse
import json
# External models import
from django.contrib.auth.models import User
# Local Models import
from .models import UserProfile, Agency
# ModelForms import
from .forms import AgencyForm


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
        # con -1 te trae el usuario actual
        # Falta contemplar cuando el id es None
        user_authenticated_id = request.user.id - 1  # if request.user.id is not None else None
        # agencies = Agency.objects.filter(user_id=user_authenticated_id).all()
        agencies = get_list_or_404(Agency, user_id=user_authenticated_id)
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
            'agency': agency
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
            agency_form = AgencyForm(request.POST)
            if agency_form.is_valid():
                # Obtener el UserProfile asociado al usuario autenticado
                # user_profile = UserProfile.objects.get(user=request.user)
                # Forma correcta preveendo si existe algun error
                user_profile = get_object_or_404(UserProfile, user=request.user)  # noqa: E501
                # Asignar el UserProfile al campo user en el formulario antes de guardar
                agency_instance = agency_form.save(commit=False)
                agency_instance.user = user_profile
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
