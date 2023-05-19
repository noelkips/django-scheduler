from django.urls import path
from .import views



urlpatterns = [
    #Events
    path('', views.view_tasks, name='view_tasks'),
    path('schedule/new/', views.add_task, name='add_task'),
    path('schedule/<int:pk>/detail/', views.schedule_detail, name="schedule_detail"),
    path('schedule/<int:pk>/edit/', views.ScheduleUpdateView.as_view(), name='update_schedule'),
    path('schedule/<int:pk>/delete/', views.ScheduleDeleteView.as_view(), name='delete_schedule'),
]
