from django.http import JsonResponse
from django.db import connection

def test_db_connection(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
            row = cursor.fetchone()
        return JsonResponse({"db": "OK", "result": row})
    except Exception as e:
        return JsonResponse({"db": "ERROR", "detail": str(e)}, status=500)
