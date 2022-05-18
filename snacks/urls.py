from django.urls import path
from .views import (HomeView,
                    SnackCreateView,
                    SnackDetailView,
                    SnackUpdateView,
                    SnackDeleteView,
                    SnackListView
                    )

urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('Create/', SnackCreateView.as_view(), name = "Snack_Create"),
    path('<int:pk>', SnackDetailView.as_view(), name = "Snack_Detail"),
    path('update/<int:pk>', SnackUpdateView.as_view(), name = "Snack_Update"),
    path('delete/<int:pk>', SnackDeleteView.as_view(), name = "Snack_Delete"),
    path('SnackList/', SnackListView.as_view(), name = "SnackList"),

]