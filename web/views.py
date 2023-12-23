from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

class TestView(APIView):
    @extend_schema(description='text')
    def get(self, request):
        if 'dj_cookie' in request.COOKIES:
            value = request.COOKIES['dj_cookie']
            return Response({"val":value})
        else:
            print("hey")
            response = Response({"status": "not set"})
            response.set_cookie(key="dj_cookie",value='dj_cookie_value', secure=True, samesite="None")
            return response
    
    def post(self, request):
        return Response({"req":"true"})


class TestView2(APIView):
    @extend_schema(description='text2')
    def get(self, request):
        return Response({"d":"e"})
    
    def post(self, request):
        return Response({"req":"true"})