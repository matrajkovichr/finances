from django.urls import path

from base import views


urlpatterns = [
    path('', views.landpage, name='landpage'),
    path('registration/', views.registration, name='registration')
]
