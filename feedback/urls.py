from django.urls import path
from .views import FeedBackView, UpdateFeedbackImageView, FeedbackWithImageAPIView, FeedbackWithoutImageAPIView

urlpatterns = [
    path('feedback', FeedBackView.as_view(), name='feedback'),
 path('feedback/update-image/<str:trainee_number>/', UpdateFeedbackImageView.as_view(), name='update-feedback-image'),
path('feedback-with-image/', FeedbackWithImageAPIView.as_view(), name='feedback_with_image'),
path('feedback-without-image/', FeedbackWithoutImageAPIView.as_view(), name='feedback_with_image'),
]
