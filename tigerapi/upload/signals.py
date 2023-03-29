from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from .models import ImageUpload, VideoUpload

@receiver(pre_delete, sender=ImageUpload)
def delete_image(sender, instance, using, **kwargs):
    instance.image.delete(save=False)

@receiver(pre_delete, sender=VideoUpload)
def delete_video(sender, instance, using, **kwargs):
    instance.video.delete(save=False)
