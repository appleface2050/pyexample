"""django_fo_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django_fo_test.views import RegisterView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
    # url(r'^accounts/login/$', auth_views.login),
    url('^', include('django.contrib.auth.urls')),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url(r'^register$', RegisterView.as_view(), name='register'),

    # url(r'^forgot-password/$', auth_views.forgot_password, name="forgot-password"),
    # url(r'^password/change/$', auth_views.password_change, name='password_change'),
    # url(r'^password/change/done/$', auth_views.password_change_done, name='password_change_done'),
    # url(r'^resetpassword/$', auth_views.password_reset, name='password_reset'),
    # url(r'^resetpassword/passwordsent/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/done/$', auth_views.password_reset_complete,name='password_reset_complete'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
]
