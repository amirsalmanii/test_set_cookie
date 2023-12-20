from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

class TestView(APIView):
    @extend_schema(description='text')
    def get(self, request):
        if 'cookie' in request.COOKIES:
            value = request.COOKIES['cookie']
            return Response({"val":value})
        else:
            response = Response({"status": "not set"})
            response.set_cookie(key="dj_cookie",value='dj_cookie_value', path="/")
            return response
    
    def post(self, request):
        return Response({"req":"true"})