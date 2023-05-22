from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class AuthAPIView(APIView):
    pass


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class AuthListAPIView(ListAPIView):
    pass

