from django.conf.urls import url
from shareIdea import views
from . import views

urlpatterns = [
    url(r'^userProfiles/$', views.userProfile_list),
    url(r'^userProfiles/(?P<pk>[0-9]+)/$', views.userProfile_detail),
    url(r'^projects/$', views.projects_list),
    url(r'^projectsDetails/$', views.project_details),
]