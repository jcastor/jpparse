from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView, TemplateView
from jpparse.models import Class, Method
from django.views.decorators.cache import cache_page
from django.db.models import Q
class ClassListView(ListView):
	model = Class
	results_per_page = 50
	paginate_by = results_per_page
	context_object_name = "class_list"
	
def searchview(request):
	query = request.GET.get('q', '')
	if query:
		qset = (Q(name__iregex=query))
		results = Class.objects.filter(qset)
	else:
		results = []

	p = dict(results=results, query=query)
	return render_to_response("jpparse/class_search.html",p, RequestContext(request))		
