from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Question
from .api import QuestionSerializer
from rest_framework.response import Response


# Create your views here.
def index(request):
    return HttpResponse("안녕하세요. shop에 오신것을 환영합니다!")


class QuestionListAPI(APIView):
    def get(self, request):
        queryset = Question.objects.all()
        print(queryset)
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)