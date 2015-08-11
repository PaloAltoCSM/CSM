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
    url(r'^admin/', include(admin.site.urls)),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/$', 'CSMWeb.views.login', name='login'),
    url(r'^logout/$', 'CSMWeb.views.logout', name='logout'),

    url(r'^weblog/', include('zinnia.urls', namespace='zinnia'), name='blog'),
    url(r'^comments/', include('django_comments.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
