from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
# Create your views here.
# def members(request):
#     return HttpResponse("Hello world!")

def members(request):
  members = Member.objects.all().values()
#   template = loader.get_template('myfirst.html')
  template = loader.get_template('allmembers.html')
  context = {
    'mymembers': members
  }
  return HttpResponse(template.render(context,request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())