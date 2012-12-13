from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView, TemplateView
from jpparse.models import Class, Method
from django.views.decorators.cache import cache_page

class ClassListView(ListView):
	model = Class
	context_object_name = "class_list"
