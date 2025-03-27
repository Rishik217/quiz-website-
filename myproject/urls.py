from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('register/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('quiz-home/', TemplateView.as_view(template_name='quiz-home.html'), name='quiz-home'),
    path('create-quiz/', TemplateView.as_view(template_name='create-quiz.html'), name='create-quiz'),
    path('quiz-preview/', TemplateView.as_view(template_name='quiz-preview.html'), name='quiz-preview'),
    path('attempted-quizzes/', TemplateView.as_view(template_name='attempted-quizzes.html'), name='attempted-quizzes'),
] 