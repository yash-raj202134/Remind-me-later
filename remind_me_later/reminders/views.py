from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Reminder
from .serializers import ReminderSerializer

# ✅ CREATE
class ReminderCreateAPIView(APIView):
    def post(self, request):
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Reminder created successfully!', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ READ (List)
class ReminderListAPIView(APIView):
    def get(self, request):
        reminders = Reminder.objects.all()
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# ✅ READ (Single)
class ReminderDetailAPIView(APIView):
    def get(self, request, id):
        reminder = get_object_or_404(Reminder, id=id)
        serializer = ReminderSerializer(reminder)
        return Response(serializer.data, status=status.HTTP_200_OK)

# ✅ UPDATE
class ReminderUpdateAPIView(APIView):
    def put(self, request, id):
        reminder = get_object_or_404(Reminder, id=id)
        serializer = ReminderSerializer(reminder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Reminder updated successfully!', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ DELETE
class ReminderDeleteAPIView(APIView):
    def delete(self, request, id):
        reminder = get_object_or_404(Reminder, id=id)
        reminder.delete()
        return Response({'message': 'Reminder deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
