
from rest_framework import viewsets, permissions
from .models import Incident
from .serializers import IncidentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all().order_by('-created_at')
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)

    @action(detail=True, methods=['post'])
    def mark_resolved(self, request, pk=None):
        inc = self.get_object()
        inc.delete()
        return Response({'status':'deleted'})
