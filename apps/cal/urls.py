from django.conf.urls import url
from . import views

app_name = 'cal'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^calendar/day/(?P<month>\w+)/(?P<year>\w+)/(?P<day>\d+)/$', views.show_day, name='show_day'),
    url(r'^calendar/yearly_view/$', views.yearly_view, name='yearly_view'),
    url(r'^calendar/change_view/$', views.change_view, name='change_view'),
    url(r'^event/new/$', views.event_new, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event'),
	url(r'^event/delete/(?P<event_id>\d+)/$', views.event_delete, name='event_delete'),
]
