from django.urls import path

from . import views

urlpatterns = [
    path('', views.submit, name='submit'),
    path('result/<unique_id>', views.result, name='result'),
]
