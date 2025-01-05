from rest_framework import viewsets, permissions
from .models import Movie
from .serializers import MovieSerializer

from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

class LoginView(TokenObtainPairView):
    pass 