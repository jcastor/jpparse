from django.conf.urls import patterns, include, url


urlpatterns = patterns('jpparse.views',
	url(r'^$', 'mainview'),
)
