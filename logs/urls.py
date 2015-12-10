from logs import views
from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns(
    'logs.views',
    url(r'^$', views.upload, name='upload'),
    url(r'^view/$', views.view, name='view'),
    url(r'^success/$', views.success, name='success'),
    url(r'^users/', views.users, name='users'),
    url(r'^mime/', views.mime, name='mime'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^status/', views.status, name='status'),
    url(r'^filter/', views.filter, name='filter'),
    url(r'^weburl/', views.weburl, name='weburl'),
    url(r'^username/', views.username, name='username'),
    url(r'^website/', views.website, name='website'),
    url(r'^data/', views.data, name='data'),
    #url(r'^logs/',views.success.html,name='success')
    #url(r'^success/$', views.success, name='success'),
	#url(r'^home/', 'myapp.views.home')
)

urlpatterns = format_suffix_patterns(urlpatterns)