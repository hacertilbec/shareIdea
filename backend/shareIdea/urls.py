from django.conf.urls import url
from shareIdea import views

urlpatterns = [
    url(r'^userProfiles/$', views.userProfile_list),
    url(r'^userProfiles/(?P<pk>[0-9]+)/$', views.userProfile_detail),
]