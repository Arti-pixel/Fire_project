from django.http import HttpResponse
from django.template import loader  
from django.shortcuts import render

def first_page(request):
    template = loader.get_template('first_page.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)

def index(request):
    template = loader.get_template('index.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)

def forms_page(request):
    return render(request, 'forms.html')
