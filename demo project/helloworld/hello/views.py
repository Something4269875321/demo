from django.http import HttpResponse
from django.db import connections, DatabaseError

def hello(request):
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT 1")
        return HttpResponse("successful connected")
    except DatabaseError:
        return HttpResponse("connection failed", status=500)
