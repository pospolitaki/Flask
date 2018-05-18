from rest_framework import generics

from apps.timelines.models import Status 
from .serializers import StatusSerializer

class StatusList(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusDetail(generics.RetrieveDestroyAPIView, generics.RetrieveUpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer