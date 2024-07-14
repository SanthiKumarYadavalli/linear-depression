from django.urls import path
from . import views

app_name = 'complaints'
urlpatterns = [
    path('add-complaint', views.add_complaint, name='add-complaint'),
    path('update-complaint', views.update_complaint, name='update-complaint')
]
