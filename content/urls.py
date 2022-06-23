from content import views
from django.urls import re_path, path

urlpatterns = [
  path('login', views.loginUser, name='login'),
  path('', views.index, name='index'),
  path('signup', views.signup, name='signup'),
  path('logout/', views.logoutUser, name='logout'),
  re_path(r'^profile/(?P<username>\w{0,50})/$', views.myprofile, name ='my_profile'),
  re_path(r'^my_neighborhoods/(?P<username>\w{0,50})/$', views.my_neighborhoods, name='my_neighborhoods'),
  re_path(r'^my_businesses/(?P<username>\w{0,50})/$', views.my_businesses, name = 'my_businesses'),
  re_path(r'^my_posts/(?P<username>\w{0,50})/$', views.my_posts, name = 'my_posts'),
  re_path(r'^(?P<username>\w{0,50})/add/neighborhood/$', views.add_neighborhood, name = 'add_neighborhood'),
  re_path(r'^(?P<username>\w{0,50})/add/business/$', views.add_business, name = 'add_business'),
  re_path(r'^(?P<username>\w{0,50})/add/post/$', views.add_post, name = 'add_post'),
  re_path(r'^(?P<username>\w{0,50})/edit/profile/$', views.editprofile, name = 'editprofile'),
  re_path(r'^(?P<username>\w{0,50})/$', views.join_neighborhood, name = 'joinneighbourhood'),
  path('search', views.search_business, name="search_results"),
  re_path(r'^neighborhood/(?P<name>\w{0,50})/$', views.single_neighborhood, name='single_neighborhood'),

]