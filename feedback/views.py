from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FeedBack
from rest_framework.pagination import PageNumberPagination
from .serializer import FeedBackSerializer, FeedBackImageUpdateSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import Q


class FeedBackPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100


class FeedBackView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        name = request.query_params.get("name", None)
        feedbacks = FeedBack.objects.all().order_by("name")

        if name:
            feedbacks = feedbacks.filter(Q(name__icontains=name))

        paginator = FeedBackPagination()
        paginated_feedbacks = paginator.paginate_queryset(feedbacks, request)
        serializer = FeedBackSerializer(paginated_feedbacks, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):

        serializer = FeedBackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        feedback_id = kwargs.get("pk")  # Get the feedback ID from the URL
        try:
            feedback = FeedBack.objects.get(id=feedback_id)
        except FeedBack.DoesNotExist:
            return Response({"error": "Feedback not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = FeedBackSerializer(feedback, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Feedback updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        feedback_id = kwargs.get("pk")  # Get the feedback ID from the URL
        try:
            feedback = FeedBack.objects.get(id=feedback_id)
        except FeedBack.DoesNotExist:
            return Response({"error": "Feedback not found"}, status=status.HTTP_404_NOT_FOUND)

        feedback.delete()
        return Response({"message": "Feedback deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class FeedBackWithID(APIView):
    def get(self, request, trainee_number):
        feedback = FeedBack.objects.filter(id=trainee_number).first()

        if not feedback:
            return Response({"error": "Feedback not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = FeedBackSerializer(feedback)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FeedbackWithImageAPIView(APIView):
    def get(self, request):
        name = request.query_params.get("name", None)
        # Filter FeedBack objects where the image field is not null
        feedbacks = FeedBack.objects.filter(image__isnull=False)

        if name:
            feedbacks = feedbacks.filter(Q(name__icontains=name))

        # Use the pagination class
        paginator = FeedBackPagination()
        paginated_feedbacks = paginator.paginate_queryset(feedbacks, request)

        # Serialize the paginated feedbacks
        serializer = FeedBackSerializer(paginated_feedbacks, many=True)

        # Return the paginated response
        return paginator.get_paginated_response(serializer.data)


class FeedbackWithoutImageAPIView(APIView):
    def get(self, request):
        # Filter FeedBack objects where the image field is not null
        feedbacks = FeedBack.objects.filter(image__isnull=True)

        # Use the pagination class
        paginator = FeedBackPagination()
        paginated_feedbacks = paginator.paginate_queryset(feedbacks, request)

        # Serialize the paginated feedbacks
        serializer = FeedBackSerializer(paginated_feedbacks, many=True)

        # Return the paginated response
        return paginator.get_paginated_response(serializer.data)


class UpdateFeedbackImageView(APIView):
    def patch(self, request, trainee_number):
        # Query for feedback using trainee_number (not unique, so we take the first match)
        feedback = FeedBack.objects.filter(trainee_number=trainee_number).first()

        if not feedback:
            return Response({"error": "Feedback not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = FeedBackImageUpdateSerializer(feedback, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Image updated successfully", "data": serializer.data},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

