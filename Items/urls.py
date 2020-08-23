from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "tasks"),
    path('update_task/<str:pk>/', views.update_task, name="update"),
    path('complete_task/<str:pk>/', views.complete_task, name="complete"),
    path('claim/', views.claim, name = "claim"),
    path('adieu/', views.adieu, name = "adieu"),
    path('register/', views.register, name='register'),
    path('view_items/', views.view_items, name='view_items'),
    path('ownership/', views.ownership, name='ownership'),
    path('qrcodes/<str:pk>/', views.qrcodes, name="qrcodes")
]