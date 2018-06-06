from django.conf.urls import url
from shareIdea import views
from . import views

urlpatterns = [
    url(r'^userProfiles/$', views.userProfile_list),
    url(r'^userProfiles/(?P<pk>[0-9]+)/$', views.userProfile_detail),
    url(r'^projects/$', views.project_list),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.project_detail),
    # url(r'^project-create/(?P<title>[a-zA-Z]+)/(?P<owner>[a-zA-Z]+)/$', views.project_create),
    # url(r'^all-users/$', views.show_users),
    # url(r'^user-register/(?P<name>[a-zA-Z]+)/(?P<surname>[a-zA-Z]+)/$', views.user_register),
    # url(r'^project-participate/(?P<title>[a-zA-Z]+)/(?P<participant>[a-zA-Z]+)/$', views.project_participate),
    url(r'^register/$', views.register),

]
