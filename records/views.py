from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from users.permissions import IsAdminUserRole, IsAnalystOrAdmin

class FinancialRecordViewSet(viewsets.ModelViewSet):
    serializer_class = FinancialRecordSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['record_type', 'category', 'date']
    ordering_fields = ['date', 'amount']

    def get_queryset(self):
        # Soft delete filter: Sirf active records hi API mein dikhenge
        return FinancialRecord.objects.filter(is_deleted=False)

    def get_permissions(self):
        # Access Control: Analyst aur Admin read kar sakte hain, create/update/delete sirf Admin
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAnalystOrAdmin]
        else:
            permission_classes = [IsAdminUserRole]
        return [permission() for permission in permission_classes]

    def perform_destroy(self, instance):
        # Soft Delete Implementation
        instance.is_deleted = True
        instance.save()