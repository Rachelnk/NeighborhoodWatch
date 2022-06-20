from content import views
from django.urls import re_path, path

urlpatterns = [
  path('login', views.loginUser, name='login'),
  path('', views.index, name='index'),
  path('signup', views.signup, name='signup'),
  path('logout', views.logoutUser, name='logout'),
  re_path(r'^profile/(?P<username>\w{0,50}/$)', views.myprofile, 'myprofile'),
  re_path(r'^myneighborhoods/(?P<username>\w{0,50}/$', views.my_neighborhoods, name='my_neighborhoods')

]