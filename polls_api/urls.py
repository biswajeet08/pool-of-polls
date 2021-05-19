from django.urls import path

from . import views

urlpatterns = [
    path('poll_results/', views.get_poll_results, name = 'poll_result_api')
    ]