from django.db import models

# Create your models here.
from django.db import models

class Reminder(models.Model):
    REMINDER_CHOICES = [
        ('SMS', 'SMS'),
        ('Email', 'Email'),
    ]
    
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_type = models.CharField(max_length=10, choices=REMINDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message} @ {self.date} {self.time} via {self.reminder_type}"
