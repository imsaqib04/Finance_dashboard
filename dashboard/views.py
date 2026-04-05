from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.permissions import IsViewerOrHigher
from .services import get_dashboard_summary

class DashboardSummaryView(APIView):
    permission_classes = [IsViewerOrHigher]

    def get(self, request):
        try:
            summary_data = get_dashboard_summary()
            return Response(summary_data)
        except Exception as e:
            return Response(
                {"error": "Failed to load dashboard data."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )