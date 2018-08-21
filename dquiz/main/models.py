from django.db import models


class Quiz(models.Model):
    quiz_description = models.CharField(max_length=100)
    isPublished = models.BooleanField()
    canPublish = models.BooleanField(default=False)

    def __str__(self):
        return self.quiz_description


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="quizes", on_delete=models.CASCADE)
    question_description = models.CharField(max_length=100)
    answer = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.question_description
