from django.conf.urls import patterns, include, url


#default view for our index
urlpatterns = patterns('cssocialprofile.views',
    url(r'^$','index', name="cssocialprofile_index"),
    )

#register and social urls
urlpatterns += patterns('',
    url(r'^logout$','django.contrib.auth.views.logout', name='cssocialprofile_logout'),
    url(r'^login$','django.contrib.auth.views.login', name='cssocialprofile_user_login'),

    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^social/', include('social_django.urls', namespace='social'))

)

#default profile edit urls
urlpatterns += patterns('cssocialprofile.views',
    url(r'^edit-profile$','edit_profile', name='cssocialprofile_edit_profile'),
    url(r'^edit-profile-photo$','edit_profile_photo', name='cssocialprofile_edit_profile_photo'),
    url(r'^edit-profile-social$','edit_profile_social', name='cssocialprofile_edit_profile_social'),
)
