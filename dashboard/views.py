from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .services import get_dashboard_summary

class DashboardSummaryView(APIView):
    # Assignment ke according Dashboard sab dekh sakte hain (Viewer, Analyst, Admin)
    permission_classes = [IsAuthenticated]

    def get(self, request):
        summary_data = get_dashboard_summary()
        return Response(summary_data)