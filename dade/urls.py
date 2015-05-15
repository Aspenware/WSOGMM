from django.conf.urls import patterns, url
from dade import views

urlpatterns = patterns('',
<<<<<<< HEAD
                       url(r'^login/', views.login, name='login'),
                       url(r'^logout/', views.logout, name='logout'),
                       url(r'^register/', views.register, name='register'),
                       url(r'^error/', views.error, name='error'),
                       )
=======
	url(r'^login/', views.login, name='login'),
	url(r'^register/', views.register, name='register'),
	url(r'^error/', views.error, name='error'),
	url(r'', views.index, name='index')
)
>>>>>>> e3a100076f4b52b7de631e7ae670f225b16c6186
