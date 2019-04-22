from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('video/<int:still_id>/', views.ProjectView.as_view(), name='still'),
]