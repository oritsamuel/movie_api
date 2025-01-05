from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, LoginView

router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'), 
]