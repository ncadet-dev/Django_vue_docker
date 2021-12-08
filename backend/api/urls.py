from django.urls import path

from . import views

urlpatterns = [
    path('public/', views.PublicView.as_view()),
    path('private/', views.PrivateView.as_view())
]