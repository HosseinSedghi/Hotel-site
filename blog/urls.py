from django.urls import path

from blog import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-page'),
]