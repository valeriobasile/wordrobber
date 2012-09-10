from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^load_test_data/', 'wrws.test_data.load_test_data'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', 'wrws.views.login'),    
    url(r'^games', 'wrws.views.games'),    
    url(r'^game/(?P<_name>.+)', 'wrws.views.game'),  
    url(r'^player/(?P<_username>.+)', 'wrws.views.player'),  
    url(r'^question', 'wrws.views.question'),  
)
