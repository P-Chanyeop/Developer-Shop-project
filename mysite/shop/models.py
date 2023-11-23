from django.db import models


# Create your models here.
class Question(models.Model):
    # 제목
    subject = models.CharField(max_length=200)
    # 내용
    content = models.TextField()
    # 작성 일시
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
