from django.urls import path
from .views import FeedBackView, UpdateFeedbackImageView, FeedbackWithImageAPIView, FeedbackWithoutImageAPIView, FeedBackWithID

urlpatterns = [
    path('feedback', FeedBackView.as_view(), name='feedback'),
path("feedback/<int:pk>/", FeedBackView.as_view(), name="feedback-detail"),
 path('feedback/update-image/<str:trainee_number>/', UpdateFeedbackImageView.as_view(), name='update-feedback-image'),
path('feedback-with-image/', FeedbackWithImageAPIView.as_view(), name='feedback_with_image'),
path('feedback-without-image/', FeedbackWithoutImageAPIView.as_view(), name='feedback_with_image'),
path('feedback-feedback-with-id/<str:trainee_number>', FeedBackWithID.as_view(), name='feedback-with-id'),
]
