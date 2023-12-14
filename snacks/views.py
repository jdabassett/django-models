from django.views.generic import ListView, DetailView
from .models import Snack

class SnackListView(ListView):
    model = Snack
    template_name = "snacks_list.html"
    context_object_name = "snacks_list"

class SnackDetailView(DetailView):
    template_name = 'snack_detailed.html'
    model = Snack
    context_object_name = 'snack_detailed'