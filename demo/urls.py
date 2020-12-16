from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_book_model_form, name='createmodel'),
    path('', views.PressureListView.as_view(), name='list')
]