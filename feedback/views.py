from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FeedBack
from rest_framework.pagination import PageNumberPagination
from .serializer import FeedBackSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class FeedBackPagination(PageNumberPagination):
    page_size = 10
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

# Create your views here.
