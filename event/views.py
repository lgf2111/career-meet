from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import EventForm
from .models import Event


# Create your views here.
class EventListView(ListView):
    model = Event
    template_name = "event/home.html"
    context_object_name = "event_list"
    ordering = ["datetime"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ["Tech", "Business"]
        return context


class EventDetailView(DetailView):
    model = Event


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventForm

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.organizer


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = "/"

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.organizer


def attend(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.attendees.add(request.user)
    return redirect("event-home")


def unattend(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.attendees.remove(request.user)
    return redirect("event-home")


def about(request):
    return render(request, "event/about.html", {"title": "About"})
