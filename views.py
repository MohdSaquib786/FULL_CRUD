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
    if request.method == 'POST':
        data = dict()
        form = ProfileForm(request.POST)
        print("here")
        print(form.errors)
        if form.is_valid():
            data['form_is_valid'] = True
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

    else:
        print("end else")
        form = ProfileForm()
    context = {'form': form}
    profileform = render_to_string('onetooneapp/profileform.html', context, request=request)
    return JsonResponse({'profile_form': profileform})


'''def newprofile(request):
    data = dict()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid:
            data['form_is_valid'] = True
            profile = Profile.object.all()
        else:
            data['notvalid'] = render_to_string('onetooneapp/profileform.html', context={'form': form}, request=request)

    else:
        form = ProfileForm()
    context = {'form': form}
    profile_form = render_to_string('onetooneapp/profileform.html', context, request=request)
    return JsonResponse({'profile_form': profile_form})'''
