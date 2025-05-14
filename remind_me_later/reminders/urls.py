
from django.urls import path
from .views import (
    ReminderCreateAPIView,
    ReminderListAPIView,
    ReminderDetailAPIView,
    ReminderUpdateAPIView,
    ReminderDeleteAPIView,
)

urlpatterns = [
    path('create/', ReminderCreateAPIView.as_view(), name='reminder-create'),
    path('', ReminderListAPIView.as_view(), name='reminder-list'),
    path('<int:id>/', ReminderDetailAPIView.as_view(), name='reminder-detail'),
    path('<int:id>/update/', ReminderUpdateAPIView.as_view(), name='reminder-update'),
    path('<int:id>/delete/', ReminderDeleteAPIView.as_view(), name='reminder-delete'),
]
