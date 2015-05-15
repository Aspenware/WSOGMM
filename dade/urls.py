from django.conf.urls import patterns, url
from dade import views

urlpatterns = patterns('',
	url(r'^login/', views.login, name='login'),
	url(r'^register/', views.register, name='register'),
	url(r'^error/', views.error, name='error'),
	url(r'', views.index, name='index')
)