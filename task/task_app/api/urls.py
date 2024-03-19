from django.urls import path

from .views import ClientListView, ClientDetailView, ProjectListView, ProjectDetailView

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-retrieve-update-destroy'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-create'),
]
