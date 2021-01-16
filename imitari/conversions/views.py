from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.decorators import api_view, permission_classes

# Create your views here.
class ConversionView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        files = request.FILES
        
        # figure out what type of image
        for f in files:
            heif_file = pyheif.read(open(f))
        # perform the conversion you just did in the shell
