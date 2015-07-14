# django imports
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.template import RequestContext
from django.db import models
from django.db.models.loading import get_model
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.core.files import File
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# python imports
from zipfile import *
import collections # for OrderedDict

# Import from general utilities
from util import *

# Import from app
from geocodingtool.settings import ROOT_APP_URL, SOTRAGE_ROOTPATH, STATIC_URL
from geocodingapp.models import *
from geocodingapp.forms import *

'''-----------------------
Home Page
-----------------------'''
# Home page
@login_required
@render_to("geocodingapp/home.html")
def home(request):
    return {}