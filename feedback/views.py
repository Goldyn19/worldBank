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
        feedbacks = FeedBack.objects.all().order_by('name')
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


class FeedbackWithImageAPIView(APIView):
    def get(self, request):
        # Filter FeedBack objects where the image field is not null
        feedbacks = FeedBack.objects.filter(image__isnull=False)

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
    def patch(self, request, name):
        # Convert name to lowercase for case-insensitive search
        name_lower = name.lower()

        try:
            # Query for feedback where the name contains the given input (case insensitive)
            feedback = FeedBack.objects.filter(Q(name__icontains=name_lower)).first()

            if not feedback:
                return Response({"error": "Feedback not found"}, status=status.HTTP_404_NOT_FOUND)

        except FeedBack.DoesNotExist:
            return Response({"error": "Feedback not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = FeedBackImageUpdateSerializer(feedback, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Image updated successfully", "data": serializer.data},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
