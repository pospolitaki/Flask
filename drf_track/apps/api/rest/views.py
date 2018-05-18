from rest_framework import generics, viewsets

from apps.timelines.models import Album, Track
from .serializers import AlbumSerializer, TrackSerializer

# class AlbumList(generics.ListCreateAPIView):
#     queryset = Album.objects.all()
#     serializer_class = AlbumSerializer

# class AlbumDetail(generics.RetrieveDestroyAPIView, generics.RetrieveUpdateAPIView):
#     queryset = Album.objects.all()
#     serializer_class = AlbumSerializer

# class TrackList(generics.ListCreateAPIView):
#     queryset = Track.objects.all()
#     serializer_class = TrackSerializer

# class TrackDetail(generics.RetrieveDestroyAPIView, generics.RetrieveUpdateAPIView):
#     queryset = Track.objects.all()
#     serializer_class = TrackSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

class TrackViewSet(viewsets.ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()
