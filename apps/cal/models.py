from django.db import models
from django.urls import reverse

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    bg_color = models.CharField(max_length=20)
    @property
    def get_html_url(self):
        start_time = self.start_time.strftime("%I:%M %p")
        end_time = self.end_time.strftime("%I:%M %p")
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {start_time}-{end_time} {self.title} </a>'