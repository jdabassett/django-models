from django.urls import path
from .views import SnackListView, SnackDetailView

urlpatterns = [
    path("snacks/", SnackListView.as_view(), name="snacks_list"),
    path("<int:pk>/", SnackDetailView.as_view(), name="snack_detailed"),
]
