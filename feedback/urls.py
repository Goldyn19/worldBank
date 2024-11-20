from django.urls import path
from .views import FeedBackView

urlpatterns = [
    path('feedback', FeedBackView.as_view(), name='feedback'),
]
