from django.urls import path
from .views import (HomeView,
                    SnackCreateView,
                    SnackDetailView,
                    SnackUpdateView,
                    SnackDeleteView
                    )

urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('create/', SnackCreateView.as_view(), name = "create_thing"),
    path('<int:pk>', SnackDetailView.as_view(), name = "detail_thing"),
    path('update/<int:pk>', SnackUpdateView.as_view(), name = "update_thing"),
    path('delete/<int:pk>', SnackDeleteView.as_view(), name = "delete_thing"),
]