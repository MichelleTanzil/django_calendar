import datetime
from django.contrib import messages
from datetime import timedelta, date, datetime as dt
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar
from .forms import EventForm
import calendar


def index(request):
    return redirect('/calendar')


class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        # Instantiate our calendar class with today's year and date
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['all_events'] = Event.objects.all()
        today = date.today()
        context['events_for_today'] = Event.objects.filter(start_time__day=today.day)
        context['today'] = today
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return dt.today()


def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
        form = EventForm(request.POST or None, instance=instance)
        return render(request, 'cal/event.html', {'form': form})
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    context={
        'form': form,
        'event': instance,
    }
    return render(request, 'cal/edit_event.html', context)

def event_new(request):
    Event.objects.create(title=request.POST['title'], description=request.POST['description'], start_time=request.POST['start_time'], end_time=request.POST['end_time'])
    return redirect('/calendar')

def event_edit(request, event_id):
    event = Event.objects.get(id=event_id)
    event.title=request.POST['title']
    event.description=request.POST['description']
    event.start_time=request.POST['start_time']
    event.end_time=request.POST['end_time']
    event.save()
    return redirect('/calendar')

def event_delete(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('/calendar')
