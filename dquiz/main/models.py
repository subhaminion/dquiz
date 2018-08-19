from django.db import models


class Quiz(models.Model):
    quiz_description = models.CharField(max_length=100)
    isPublished = models.BooleanField()

    def __str__(self):
        return f"{self.quiz_description}"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="quizes")
    question_description = models.CharField(max_length=100)
    answer = models.CharField(blank=True, max_length=100)
