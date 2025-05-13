from django.urls import path
from .views import ReminderCreateAPIView

urlpatterns = [
    path('reminders/', ReminderCreateAPIView.as_view(), name='create-reminder'),
]
