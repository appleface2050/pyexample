from django.conf.urls import url

from . import views
app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lgoin_view$', views.lgoin_view, name='lgoin_view'),
    url(r'^logout_view$', views.logout_view, name='logout_view'),
    url(r'^my_view$', views.my_view, name='my_view'),



    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),




]