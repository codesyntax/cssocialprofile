from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template

from registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.views import password_reset


urlpatterns = patterns('cssocialprofile.views',
    url(r'^$','index', name="cssocialprofile_index"),
    )

urlpatterns += patterns('',
    (r'^accounts/', include('registration.urls')),
    (r'^social/', include('social_auth.urls')),
    url(r'^logout$','django.contrib.auth.views.logout', name='cssocialprofile_logout'),
    url(r'^login$','django.contrib.auth.views.login', name='cssocialprofile_user_login'),
)


"""

urlpatterns += patterns('',
    #(r'^accounts/', include('registration.urls')),
    #(r'^social/', include('social_auth.urls')),
    #url(r'^login$','django.contrib.auth.views.login', name='cssocialprofile_user_login'),
    
    

    url(r'^password_reset$',
        'django.contrib.auth.views.password_reset',
        {'template_name':'registration/password_reset.html'},
        name='cssocialprofile_password_reset'),
    url(r'^password_reset_done$',
        'django.contrib.auth.views.password_reset_done',
        {'template_name':'registration/password_reset_done.html'},
        name='cssocialprofile_password_reset_done'),                       
    url(r'^password_reset_confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name':'registration/password_reset_confirm.html'},
        name='cssocialprofile_password_reset_confirm'),
    url('^password_reset_complete',
        'django.contrib.auth.views.password_reset_complete',
        {'template_name':'registration/password_reset_complete.html'},
        name='cssocialprofile_password_reset_complete'),
    url('^register','registration.views.register',{'success_url':'/erabiltzaileak/aktibatu','form_class':RegistrationFormUniqueEmail},name='cssocialprofile_register'),
    url('^activate/(?P<activation_key>\w+)$','registration.views.activate',name='cssocialprofile_activate'),
    url('^registration_complete$',direct_to_template,{'template':'registration/registration_complete.html'},name='cssocialprofile_registration_complete'),
)
"""


urlpatterns += patterns('cssocialprofile.views',    
    url(r'^(?P<username>[^/]+)$','user_index', name='cssocialprofile_user_index'),
    url(r'^(?P<username>[^/]+)$','user_edit', name='cssocialprofile_user_edit'),    

)





"""
    #(r'^aktualitatea/', include('cscontent.base.urls')),

    #login eta logout loturetan next=*** parametroa jarrita berbideraketa egiten da
    url(r'^erabiltzaileak$','django.contrib.auth.views.login', name='erabiltzailea_user_login'),                      
    url(r'^erabiltzaileak/irten$','django.contrib.auth.views.logout', name='erabiltzailea_user_logout'),
    #Pasahitza berrezarri
    url(r'^erabiltzaileak/pasahitza_aldatu$',
        'django.contrib.auth.views.password_reset',
        {'template_name':'registration/password_change.html','post_reset_redirect':'/erabiltzaileak/pasahitza_nola_aldatu'},
        name='erabiltzailea_user_password_reset'),
    url(r'^erabiltzaileak/pasahitza_nola_aldatu$',
        'django.contrib.auth.views.password_reset_done',
        {'template_name':'registration/password_change_ok.html'},
        name='erabiltzailea_user_password_reset_done'),                       
    url(r'^erabiltzaileak/eskaera_ziurtatu/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name':'registration/reset_password_verified.html','post_reset_redirect':'/erabiltzaileak/pasahitza_ondo_aldatuta'},
        name='erabiltzailea_password_reset_confirm'),
    url('^erabiltzaileak/pasahitza_ondo_aldatuta',
        'django.contrib.auth.views.password_reset_complete',
        {'template_name':'registration/password_change_done.html'},
        name='erabiltzaileak_password_reset_ok'),
    #/pasahitza berrezarri
    #Izena eman
    url('^erabiltzaileak/izena_eman','registration.views.register',{'success_url':'/erabiltzaileak/aktibatu','form_class':RegistrationFormUniqueEmail},name='erabiltzaileak_izena_eman'),
    url('^erabiltzaileak/aktibatu/(?P<activation_key>\w+)$','registration.views.activate',name='erabiltzailea_aktibatu'),
    url('^erabiltzaileak/aktibatu$',direct_to_template,{'template':'registration/registration_complete.html'},name='erabiltzailea_aktibatu_nola'),
    #/izena eman
    
    #/social links    
    (r'^erabiltzaileak/social/', include('social_auth.urls')),    

    #Perfilak aldatu
    (r'^erabiltzaileak/perfila/', include('uztarria.profile.urls')),    
"""  





