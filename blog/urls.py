from django.urls import path

from blog import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-page'),
    path('contact-us/', views.TicketView.as_view(), name='ticket-page'),
]