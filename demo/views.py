from django.shortcuts import render
import json
from .models import Agency


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


#----------- Agency CRUD -----------#
def list_agency(request):
    agencies = Agency.objects.all()
    context = {
        "agencies": agencies
    }
    return render(
        request=request,
        template_name='demo/crud/agency/list_agency.html',
        context=context
    )


def update_agency(request):
    return render(
        request=request,
        template_name='demo/crud/agency/update_agency.html'
    )


def register_agency(request):
    return render(
        request=request,
        template_name='demo/crud/agency/register_agency.html'
    )


def delete_agency(request):
    return render(
        request=request,
        template_name='demo/crud/agency/delete_agency.html'
    )


#----------- End of Agency CRUD -----------#