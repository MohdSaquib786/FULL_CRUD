from profile import Profile

from django.core.serializers import json
from django.template.loader import render_to_string

from onetooneapp.form import ProfileForm
from onetooneapp.models import *
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def join(request):
    return HttpResponse("working")


def index(request):
    return render(request, 'onetooneapp/index.html', {})


def createprofile(request):
    data = dict()
    #------------------------------IT will be call when request will be post and when form will be 'submited htmlpage is profileform.html'
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        print("here")
        print(form.errors)
        if form.is_valid():
            data['form_is_valid'] = True
            print("form is valid")
            form.save()
            profileobj = Profile.objects.all()
            context = {'profiles': profileobj}
            data['profile_list'] = render_to_string('onetooneapp/profilelist.html', context, request=request)
            return JsonResponse(data)
        else:
            print("form else execute")
            data['form_not_valid']: False
            context = {'form': form}
            data['profile_form'] = render_to_string('onetooneapp/profileform.html', context, request=request)
            return JsonResponse(data)
#-------------------------------------end request post of " profileform.html"

    #----------------------------It will be call first time when page will be loaded callin by fun() with firstrequest key
    elif(request.method=="GET" and request.GET.get('firstrequest')=='yes'):
        profileobj = Profile.objects.all()
        context = {'profiles': profileobj}
        print("undefine")
        data['profile_list'] = render_to_string('onetooneapp/profilelist.html', context, request=request)
        print("undefine")
        return JsonResponse(data)
    #-----------------------------end first time loaded all data

    #------------------------------ it will be call for open the form on click of ADDPROFILE BUTTON with the key of openform
    elif(request.method=="GET" and request.GET.get('openform')=='openform'):
        print("end else")
        form = ProfileForm()
    context = {'form': form}
    profileform = render_to_string('onetooneapp/profileform.html', context, request=request)
    return JsonResponse({'profile_form': profileform})
    #----------------------------------------------------------end for open form

def profile_update(request, pk):
    print("profile_updated")
    data = dict()
    form = ProfileForm()
    print("profile_updated1")
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            print("form is valid")
            data['form_is_valid'] = True
            print(form.cleaned_data.items())
            user = form.cleaned_data['user']
            print(user)
            designation = form.cleaned_data['designation']
            print(designation)
            country = form.cleaned_data['country']
            print(country)
            profile = Profile.objects.filter(pk=pk)
            for i in profile:
                i.user=user
                i.designation=designation
                i.country=country
                i.save()
            return JsonResponse(data)
        else:
            data['form_is_invalid'] = False
            context = {'form': form}
            data['profile_form_update'] = render_to_string('onetooneapp/partialbookupdate.html', context,
                                                           request=request)
            print("nowdays")
            print(form.errors)
            return JsonResponse(data)

    else:
        obj = Profile.objects.filter(pk=int(pk))
        for i in obj:
            form = ProfileForm(initial={'user': i.user, 'designation': i.designation, 'country': i.country})
            print(form)
        context = {'form': form,
                   'id': pk}
        print("profile_updated2")
        data['profile_update_form'] = render_to_string('onetooneapp/partialbookupdate.html', context, request=request)
        print("profile_updated3")
        return JsonResponse(data)
def profile_delete(request,pk):
    deleteobj=Profile.objects.filter(pk=pk).delete()
    if(deleteobj):
        return JsonResponse({'status':'success'})

