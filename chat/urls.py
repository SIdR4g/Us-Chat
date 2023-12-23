from django.urls import path

from . import views

urlpatterns = [
    path('join_room/', views.rooms, name='rooms'),
    path('', views.options, name = 'options' ),
    path('create_room/', views.create_chat_room, name = 'create'),
    path('<slug:slug>/', views.room, name='room'),
]