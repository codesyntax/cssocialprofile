from django.template import RequestContext
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from photologue.models import Photo
from cssocialprofile.forms import ProfileForm, ProfilePhotoForm
from cssocialprofile.utils.slug import time_slug_string
from django.utils.translation import ugettext as _

from .models import get_profile_model


def index(request):
    h = {}
    return render(request, 'cssocialprofile/base.html', h)



@login_required
def edit_profile(request):
    tab = 'personal'
    user = request.user
    profile_model = get_profile_model()
    profile = getattr(user, profile_model.__name__.lower())
    if request.method == 'POST':
        posta = request.POST.copy()
        profileform = ProfileForm(posta, instance=profile)
        if profileform.is_valid():
            profileform.save()
            messages.add_message(request, messages.SUCCESS, _('New user data saved.'), fail_silently=True)
            return HttpResponseRedirect(reverse('cssocialprofile_edit_profile'))
    else:
        profileform = ProfileForm(instance=profile)

    return render(request, 'profile/edit_personal.html', locals())


def handle_uploaded_file(f, title):
    photo = Photo()
    photo.title = u'%s %s' % (title, time_slug_string())
    photo.slug = time_slug_string()
    photo.image = f
    photo.save()
    return photo


@login_required
def edit_profile_photo(request):
    tab = 'photo'
    user = request.user
    profile_model = get_profile_model()
    profile = getattr(user, profile_model.__name__.lower())
    if request.method == 'POST':
        form = ProfilePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = handle_uploaded_file(request.FILES['avatarpic'], profile.get_fullname())
            profile.photo = photo
            profile.save()

    else:
        form = ProfilePhotoForm()
    return render(request, 'profile/edit_photo.html', locals())


@login_required
def edit_profile_social(request):
    tab = 'social'
    user = request.user
    profile_model = get_profile_model()
    profile = getattr(user, profile_model.__name__.lower())
    return render(request, 'profile/edit_social.html', locals())
