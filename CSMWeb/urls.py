from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'CSMWeb.views.index', name='index'),
    url(r'^about/', 'CSMWeb.views.about', name='about'),
    url(r'^projects/', 'CSMWeb.views.projects', name='projects'),
    url(r'^members/', 'CSMWeb.views.members', name='members'),
    url(r'^inspirations/', 'CSMWeb.views.inspirations', name='inspirations'),
    url(r'^addproj/', 'CSMWeb.views.addproj', name='addproj'),
    url(r'^joinproj/', 'CSMWeb.views.joinproj', name='joinproj'),
    url(r'^followproj/', 'CSMWeb.views.followproj', name='followproj'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reg_query/$', 'CSMWeb.views.reg_query', name='reg_query'),
    url(r'^reg_connect/$', 'CSMWeb.views.reg_connect'),
    url(r'^reg_remove/$', 'CSMWeb.views.reg_remove'),
    url(r'^reg/$', 'CSMWeb.views.reg'),
    url(r'^regp/$', 'CSMWeb.views.regp'),
    url(r'^reg_config/$', 'CSMWeb.views.reg_config'),
    url(r'^reg_becomeguide/$', 'CSMWeb.views.reg_becomeguide'),
    url(r'^reg_notification/$', 'CSMWeb.views.reg_notification'),
    #
    url(r'^requestform/$', 'CSMWeb.views.requestform'),
    url(r'^reg_addrequest/$', 'CSMWeb.views.reg_addrequest'),
    url(r'^reg_getrequests/$', 'CSMWeb.views.reg_getrequests', name='get_requests'),
    url(r'^reg_getguides/$', 'CSMWeb.views.reg_getguides', name='get_guides'),
    url(r'^reg_addguide/$', 'CSMWeb.views.reg_addguide', name='add_guide'),
    url(r'^reg_getsessions/$', 'CSMWeb.views.reg_getsessions', name='get_sessions'),
    url(r'^reg_addsession/$', 'CSMWeb.views.reg_addsession', name='add_session'),
    #
    url(r'^reg_setNotification/$', 'CSMWeb.views.reg_setNotification'),
    url(r'^reg_getNotification/$', 'CSMWeb.views.reg_getNotification'),
    url(r'^reg_delNotification/$', 'CSMWeb.views.reg_delNotification'),
    url(r'^mapview/$', 'CSMWeb.views.mapview', name='mapview'),
    url(r'^globeview/$', 'CSMWeb.views.globeview', name='globeview'),

    url(r'^admin/', include(admin.site.urls)),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/$', 'CSMWeb.views.login', name='login'),
    url(r'^logout/$', 'CSMWeb.views.logout', name='logout'),

    url(r'^weblog/', include('zinnia.urls', namespace='zinnia'), name='blog'),
    url(r'^comments/', include('django_comments.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
