from django.urls import path

from . import views

urlpatterns = [
    path('pool/', views.pool, name='pool'),
    path('', views.homepage, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('sports/', views.sports, name = 'sports'),
    path('bollywood/', views.bolly, name = 'bolly'),
    path('technology/', views.tech, name = 'tech'),
    path('misc/', views.misc, name = 'misc'),
    path('results/<poll_id>/', views.results, name = 'results'),
    path('result/', views.result, name = 'result'),
    path('create_poll/', views.create_poll, name = 'create_poll'),
    path('poll/create/polls_api/', views.poll_create_api, name = 'poll_create_api')
]