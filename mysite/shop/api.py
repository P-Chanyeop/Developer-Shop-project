# 모델을 사용하기 위해 모델 임포트
from .models import Question, Answer
# rest api를 사용하기 위해 rest_framework 임포트
from rest_framework import serializers, viewsets


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
