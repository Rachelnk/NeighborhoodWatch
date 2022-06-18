from content import views
from django.urls import re_path, path

urlpatterns = [
  path('login', views.loginUser, name='login'),
  path('', views.index, name='index'),
  path('signup', views.signup, name='signup'),
  path('logout', views.logoutUser, name='logout')
]