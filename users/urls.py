"""define the URL patterns for users . """

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
      # Login page
      url(r'^login/$',login,{'template_name':'users/login.html'},
            name='login'),
      # Logout page
      url(r'^logout/$',views.logut_view,name='logout'),

      # Register page
      url(r'^register$', views.register , name='register'),

]
