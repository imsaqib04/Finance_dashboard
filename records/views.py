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
    ordering_fields = ['date', 'amount']        # addition self

    search_fields = ['category', 'notes']

    def get_queryset(self):
        # User API url mein bhej sakta hai: /api/records/?show_deleted=true
        show_deleted = self.request.query_params.get('show_deleted', 'false').lower() == 'true'
        
        # Agar user Analyst/Admin hai AUR usne show_deleted=true bheja hai
        if show_deleted and self.request.user.role in ['ANALYST', 'ADMIN']:
            return FinancialRecord.objects.all() # Sab dikhao (Deleted bhi)
            
        # Default behavior: Sirf active records dikhao
        return FinancialRecord.objects.filter(is_deleted=False)

    def get_permissions(self):
        # Access Control: Analyst aur Admin read kar sakte hain, create/update/delete sirf Admin
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAnalystOrAdmin]
        else:
            permission_classes = [IsAdminUserRole]
        return [permission() for permission in permission_classes]
    
    #  Record save hone se pehle logged-in user attach karo
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_destroy(self, instance):
        # Soft Delete Implementation
        instance.is_deleted = True
        instance.save()