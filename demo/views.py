from django.shortcuts import render
import json


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
