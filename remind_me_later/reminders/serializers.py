from datetime import timezone
from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'

    def validate_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("The date must be in the future.")
        return value

    def validate_time(self, value):
        if value < timezone.now().time():
            raise serializers.ValidationError("The time must be in the future.")
        return value