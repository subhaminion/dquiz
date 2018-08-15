from django.db import models


class Quiz(models.Model):
    description = models.CharField(max_length=100)
    isPublished = models.BooleanField()

    def __str__(self):
        return f"{self.description}"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="quizes")
    description = models.CharField(max_length=100)
    answer = models.CharField(blank=True, max_length=100)
