from django.urls import path
from .views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
)
from . import views

urlpatterns = [
    path("", EventListView.as_view(), name="event-home"),
    path("event/create/", EventCreateView.as_view(), name="event-create"),
    path("event/<int:pk>/", EventDetailView.as_view(), name="event-detail"),
    path("event/<int:pk>/update", EventUpdateView.as_view(), name="event-update"),
    path("event/<int:pk>/delete", EventDeleteView.as_view(), name="event-delete"),
    path("event/<int:pk>/attend", views.attend, name="event-attend"),
    path("event/<int:pk>/unattend", views.unattend, name="event-unattend"),
    path("about/", views.about, name="event-about"),
]
