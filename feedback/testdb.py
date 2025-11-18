from django.urls import path
from django.http import JsonResponse
from django.db import connection

def test_db(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({"db": "CONNECTED"})
    except Exception as e:
        return JsonResponse({"db": "ERROR", "details": str(e)}, status=500)

urlpatterns = [
    path("", test_db),
]
