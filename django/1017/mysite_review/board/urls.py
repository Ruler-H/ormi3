from django.urls import path
from . import views

urlpatterns = [
    path('', views.board, name='board'),
    path('<int:pk>/', views.post, name='post'),
    path('tag/<str:tag>/', views.tag, name='tag'),
]