from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import generate_random_json


class PublicView(APIView):
    """A view which is accessed publicly."""
    def get(self, request):
        return Response(generate_random_json())


class PrivateView(APIView):
    """A view that is protected."""
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        return Response(generate_random_json())