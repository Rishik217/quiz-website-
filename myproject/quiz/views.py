from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Quiz, Question, Answer
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer

# Template Views
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('quiz-home')
    return render(request, 'registration/login.html')

@login_required
def quiz_home(request):
    return render(request, 'quiz-home.html')

# API Views
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        quiz = self.get_object()
        questions = quiz.questions.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def submit_attempt(self, request, pk=None):
        quiz = self.get_object()
        answers = request.data.get('answers', [])
        score = 0
        total_questions = quiz.questions.count()
        
        for answer in answers:
            question_id = answer.get('question_id')
            selected_answer_id = answer.get('answer_id')
            
            try:
                question = Question.objects.get(id=question_id, quiz=quiz)
                if question.answers.get(id=selected_answer_id).is_correct:
                    score += 1
            except (Question.DoesNotExist, Answer.DoesNotExist):
                continue
        
        return Response({
            'score': score,
            'total_questions': total_questions,
            'percentage': (score / total_questions) * 100 if total_questions > 0 else 0
        })