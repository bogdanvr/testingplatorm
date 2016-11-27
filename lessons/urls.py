from django.conf.urls import patterns, url

from lessons import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^lessons/(?P<lesson_id>\d+)/$', views.lesson, name='lesson'),
    url(r'^problems/(?P<problem_id>\d+)/$', views.problem, name='problem'),
    url(r'^send_submission/(?P<problem_id>\d+)/$', views.send_submission, name='send_submission'),
    url(r'^load_submissions/$', views.load_submissions, name='load_submissions'),
    url(r'^register/$', views.register, name='register'),
    url(r'^calc/$', views.calcview, name='calc'),
    url(r'^load_calc/$', views.load_calc, name='load_calc'),
    url(r'^needratinglist/$', views.load_calc, name='NeedratingList'),
    url(r'^time/$', views.current_datetime, name='time'),
    url(r'^hello/', views.hello, name='hello'),
    url(r'^home/', views.home, name='home'),
    url(r'^calcutta/', views.calcutta, name='calcutta'),


)
