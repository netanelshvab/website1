from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def memberss(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_member_task.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context, request))

def WEBSITEhome(request):
    template = loader.get_template('mysecondHTML.html')
    return HttpResponse(template.render())

def about_me(request):
    template = loader.get_template('about-me.html')
    return HttpResponse(template.render())

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))