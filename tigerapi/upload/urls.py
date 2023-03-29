from django.urls import path
from . import views

urlpatterns = [
    path('upload/image/', views.UploadImageView.as_view()),
    path('upload/image/<int:id>/', views.UploadImageView.as_view()),
    path('upload/video/', views.UploadVideoView.as_view()),
    path('upload/video/<int:id>/', views.UploadVideoView.as_view())
]
