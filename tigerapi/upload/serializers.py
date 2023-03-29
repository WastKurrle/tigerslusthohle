from rest_framework import serializers
from .models import ImageUpload, VideoUpload


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload

        fields = (
            'id',
            'title',
            'image',
            'get_image',
            'description'
        )


class VideoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoUpload

        fields = (
            'id',
            'title',
            'video',
            'description',
            'get_video',
        )
