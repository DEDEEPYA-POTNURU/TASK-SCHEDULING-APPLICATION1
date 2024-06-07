from django.urls import path 
from .  import views

urlpatterns = [
    path('create/', views.Board_create, name='Board_create'),
    # path('<int:pk>/update/', views.GoogleForm_update, name='GoogleForm_update'),
    # path('<int:pk>/delete/', views.GoogleForm_delete, name='GoogleForm_delete'),
     
]