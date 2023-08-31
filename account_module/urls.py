from django.urls import path

from account_module import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login-page'),
    path('logout/', views.Logout.as_view(), name='logout-page'),
]