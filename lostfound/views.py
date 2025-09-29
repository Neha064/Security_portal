
from rest_framework import viewsets, permissions
from .models import LostItem
from .serializers import LostItemSerializer

class LostItemViewSet(viewsets.ModelViewSet):
    queryset = LostItem.objects.all().order_by('-created_at')
    serializer_class = LostItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)
