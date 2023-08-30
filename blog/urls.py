from django.urls import path

from blog import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-page'),
    path('contact-us/', views.TicketView.as_view(), name='ticket-page'),
    path('rooms/', views.RoomListView.as_view(), name='room-page'),
    path('gallery/', views.GalleryView.as_view(), name='gallery-page'),
    path('blog/', views.BlogView.as_view(), name='blog-page'),
]