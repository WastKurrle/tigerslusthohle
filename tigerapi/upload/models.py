from django.db import models


class ImageUpload(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_image(self):
        return 'http://127.0.0.1:8000' + self.image.url


class VideoUpload(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='uploads/')
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_video(self):
        return 'http://127.0.0.1:8000' + self.video.url
