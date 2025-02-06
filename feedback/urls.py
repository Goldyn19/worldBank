from django.urls import path
from .views import FeedBackView, UpdateFeedbackImageView

urlpatterns = [
    path('feedback', FeedBackView.as_view(), name='feedback'),
 path('feedback/update-image/<str:name>/', UpdateFeedbackImageView.as_view(), name='update-feedback-image'),
]
