from django.urls import path
from polls import views

urlpatterns = [
    path('polls/', views.polls_list, name='polls-list'),
    path('polls/<int:pk>/', views.polls_detail, name='polls_detail'),
]
