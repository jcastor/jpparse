from django.shortcuts import render_to_response
from django.template import RequestContext
def mainview(request):
	return render_to_response("jpparse/index.html", RequestContext(request))
