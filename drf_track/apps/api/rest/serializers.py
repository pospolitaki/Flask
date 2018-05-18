from rest_framework import serializers
from apps.timelines.models import Album, Track

class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = ('duration','order', 'title')

class AlbumSerializer(serializers.ModelSerializer):
    #tracks = serializers.StringRelatedField(many=True)
    #tracks = serializers.PrimaryKeyRelatedField(many=True, queryset=Track.objects.all())
    # ??tracks = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='track-detail',
    #     lookup_field='pk'
    # )
    # tracks = serializers.SlugRelatedField(
    #     many=True,
    #     slug_field='title',
    #     queryset=Track.objects.all()
    #  )

    tracks = TrackSerializer(many=True)

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')

        

