from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^logs/', include('logs.urls', namespace="logs")),
    url(r'^admin/', include(admin.site.urls)),
)
