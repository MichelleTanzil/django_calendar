from django.conf.urls import url
from . import views

app_name = 'cal'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/$', views.event, name='event'),
    url(r'^event/new/$', views.event_new, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
	url(r'^event/delete/(?P<event_id>\d+)/$', views.event_delete, name='event_delete'),
]
