from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_list_or_404

from django.contrib.contenttypes.models import ContentType

#from cssocialprofile.models import *

def index(request):
    """ """
    h = {}
    return render_to_response('base.html', h, context_instance=RequestContext(request))
    
def user_index(request, username):
    """ """
    h = {}
    return render_to_response('base.html', h, context_instance=RequestContext(request))    
    
def user_edit(request, username):
    """ """
    h = {}
    return render_to_response('base.html', h, context_instance=RequestContext(request))        