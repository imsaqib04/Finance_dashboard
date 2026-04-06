from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from .filters import FinancialRecordFilter
from users.permissions import IsAdminUserRole, IsAnalystOrAdmin, IsViewerOrHigher
from users.models import User


class FinancialRecordViewSet(viewsets.ModelViewSet):
    serializer_class = FinancialRecordSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = FinancialRecordFilter
    search_fields = ['category', 'notes']
    ordering_fields = ['date', 'amount']

    def get_queryset(self):
        show_deleted = self.request.query_params.get('show_deleted', 'false').lower() == 'true'
        
        if show_deleted and self.request.user.role in [
            User.Role.ANALYST, 
            User.Role.ADMIN
        ]:
            return FinancialRecord.objects.all()
            
        return FinancialRecord.objects.filter(is_deleted=False)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAnalystOrAdmin]
        else:
            permission_classes = [IsAdminUserRole]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {
                    "success": True,
                    "message": "Financial record added successfully!",
                    "data": serializer.data
                }, 
                status=status.HTTP_201_CREATED, 
                headers=headers
            )
        return Response(
            {
                "success": False,
                "message": "Failed to add record. Please check the data.",
                "errors": serializer.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(
                {
                    "success": True,
                    "message": f"Financial Record ID {instance.id} updated successfully!",
                    "data": serializer.data
                }, 
                status=status.HTTP_200_OK
            )
            
        return Response(
            {
                "success": False,
                "message": "Failed to update record. Please check the data.",
                "errors": serializer.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {
                "success": True,
                "message": f"Record ID {instance.id} soft-deleted successfully!"
            }, 
            status=status.HTTP_200_OK
        )