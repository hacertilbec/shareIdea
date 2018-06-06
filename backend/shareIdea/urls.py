from django.conf.urls import url
from shareIdea import views
from . import views

urlpatterns = [
    url(r'^userProfiles/$', views.userProfile_list),
    url(r'^userProfiles/(?P<pk>[0-9]+)/$', views.userProfile_detail),
    url(r'^projects/$', views.project_list),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.project_detail),

]
