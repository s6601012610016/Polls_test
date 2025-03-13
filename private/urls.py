from django.urls import path

from . import views

app_name = "private"
urlpatterns = [
    path("private/", views.IndexView.as_view(), name="index"),
    path("private/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("private/<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("private/<int:question_id>/vote/", views.vote, name="vote"),
]