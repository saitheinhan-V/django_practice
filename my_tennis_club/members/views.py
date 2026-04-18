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

#queryset = Member.objects.all() #select * from members
#queryset = Member.objects.filter(firstname="John") #select * from members where firstname="John"
#queryset = Member.objects.get(id=1) #select * from members where id=1
#mydata = Member.objects.filter(lastname='Refsnes', id=2).values() #select * from members where lastname='Refsnes' and id=2
#mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values() #select * from members where firstname='Emil' or firstname='Tobias' 
#using Q
#from django.db.models import Q
#mydata = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values() #select * from members where firstname='Emil' or firstname='Tobias'   


#mydata = Member.objects.filter(firstname__startswith='L').values() #select * from members where firstname like 'L%'
#mydata = Member.objects.filter(firstname__endswith='s').values() #select * from members where firstname like '%s'
#mydata = Member.objects.filter(firstname__contains='oh').values() #select * from members where firstname like '%oh%'

#mydata = Member.objects.all().order_by('firstname').values() #select * from members order by firstname asc
#mydata = Member.objects.all().order_by('-firstname').values() #select * from members order by firstname desc

#mydata = Member.objects.all().order_by('-firstname').values() #select * from members order by firstname desc
#mydata = Member.objects.all().order_by('lastname', '-id').values() #select * from members order by lastname asc, id desc