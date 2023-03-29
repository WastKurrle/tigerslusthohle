from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ImageUploadSerializer, VideoUploadSerializer
from .models import ImageUpload, VideoUpload


class UploadImageView(APIView):
    def get(self, request):
        uploads = ImageUpload.objects.all()
        serializer = ImageUploadSerializer(uploads, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)
        serializer.is_valid()

        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        instance = ImageUpload.objects.get(id=id)

        if instance == None:
            return Response(status=404)

        instance.delete()
        return Response(status=200)



class UploadVideoView(APIView):
    def get(self, request):
        uploads = VideoUpload.objects.all()
        serializer = VideoUploadSerializer(uploads, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VideoUploadSerializer(data=request.data)
        serializer.is_valid()

        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        instance = VideoUpload.objects.get(id=id)

        if instance == None:
            return Response(status=404)

        instance.delete()
        return Response(status=200)
