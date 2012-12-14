from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, TemplateView
from jpparse.models import Class, Method
from jpparse.views import ClassListView
from django.views.decorators.cache import cache_page
urlpatterns = patterns('jpparse.views',
	url(r'^$',TemplateView.as_view(template_name="jpparse/info.html"), name="main"),
	url(r'^info/$', TemplateView.as_view(template_name="jpparse/info.html"), name="info"),
	url(r'^classes/search/$', TemplateView.as_view(template_name="jpparse/info.html"), name="class_list_search"),
	url(r'^classes/$', ClassListView.as_view(), name="class_list_view"),
#	url(r'^classes/(?P<rpp>\d+)/$', ClassListView.as_view(), name="class_rpp_list_view"),
#	url(r'^classes/$', cache_page(ClassListView.as_view(), 60*10), name="class_list_view"),
	url(r'^class/(?P<pk>\d+)/$', DetailView.as_view(model=Class,), name="class_detail_view"),
	url(r'^method/(?P<pk>\d+)/$', DetailView.as_view(model=Method,), name="method_detail_view"),
)
