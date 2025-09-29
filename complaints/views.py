
from rest_framework import viewsets, permissions
from .models import Complaint
from .serializers import ComplaintSerializer
from rest_framework.response import Response

class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all().order_by('-created_at')
    serializer_class = ComplaintSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(filer=self.request.user)
