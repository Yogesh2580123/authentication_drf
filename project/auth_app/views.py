from .models import RegisterUser
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from post_app.models import Post
from post_app.serializers import PostSerializer

class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer



class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff or user.is_superuser:
                post_data = Post.objects.all()
            else:
                post_data = Post.objects.filter(create_by=user)
            
            post_serializer = PostSerializer(post_data, many=True)
            refresh = RefreshToken.for_user(user=user)
            return Response({
                "refresh" : str(refresh),
                "access" : str(refresh.access_token),
                "login status": "User login successfully...",
                "user" : username,
                "user_data" : post_serializer.data
            })
        else:
            return Response({"user": "this user credential has not valid"}, status=status.HTTP_401_UNAUTHORIZED)