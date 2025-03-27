from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, login_view, quiz_home

# Create a router and register your viewsets with it
router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)  # Removed basename

# Define your URL patterns
urlpatterns = [
    # Template Views
    path('login/', login_view, name='login'),
    path('quiz-home/', quiz_home, name='quiz-home'),
    
    # API endpoints
    path('api/', include(router.urls)),
]
