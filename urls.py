from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from jpparse.models import Class, Method

urlpatterns = patterns('jpparse.views',
	url(r'^$', 'mainview'),
	url(r'^classes/$', ListView.as_view(model=Class,context_object_name="class_list",), name="class_list_view"),
	url(r'^classes/(?P<pk>\d+)/$', DetailView.as_view(model=Class,), name="class_detail_view"),
	url(r'^method/(?P<pk>\d+)/$', DetailView.as_view(model=Method,), name="method_detail_view"),
)
