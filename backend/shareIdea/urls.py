from django.conf.urls import url
from shareIdea import views

urlpatterns = [
    url(r'^userProfiles/$', views.userProfile_list),
    url(r'^registerUser/', views.registerUser),
    url(r'^userProfiles/(?P<pk>[0-9]+)/$', views.userProfile_detail),
    url(r'^loginUser/$', views.loginUser),

    url(r'^projects/$', views.project_list),
    url(r'^addProject/$', views.addProject),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.project_detail),

]