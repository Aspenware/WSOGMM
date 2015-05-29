from django.conf.urls import patterns, include, url
from django.contrib import admin
import dade.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WSOGMM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'site/', include(dade.urls)),
    #url(r'', include(dade.urls))
)
