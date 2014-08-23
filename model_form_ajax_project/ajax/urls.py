from django.conf.urls import patterns, url


urlpatterns = patterns(
    'ajax.views',
    url(r'^$', 'feedback'),
    url(r'^create_feedback/', 'create_feedback')
)
