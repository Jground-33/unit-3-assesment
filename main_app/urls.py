from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.CreateWish.as_view(), name='add'),
    path('delete/<int:pk>', views.DeleteWish.as_view(), name='delete'),
]
