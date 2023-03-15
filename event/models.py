from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    datetime = models.DateTimeField()
    image = models.ImageField(upload_to="event_pics", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(User, related_name="attendees", blank=True)
    # group

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event-detail", kwargs={"pk": self.pk})
