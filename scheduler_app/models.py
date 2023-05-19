from django.db import models
from django.utils import timezone
import os


def event_image(instance, filename):
    upload_to = 'media/'
    ext = filename.split('.')[-1]
    filename = 'schedule/{}.{}'.format(instance.title, ext)
    return os.path.join(upload_to, filename)


class Schedule(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    image = models.ImageField(upload_to=event_image, blank=False, null=False, verbose_name='Tiff image')

    def days_remaining(self):
        current_date = timezone.now()
        remaining_time = self.start_time - current_date
        days_remaining = remaining_time.days
        return days_remaining
    
    def __str__(self):
        return self.title[:50]


