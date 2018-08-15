from django.forms import ModelForm
from main.models import Quiz, Question


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['id', 'description', 'isPublished']


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['description', 'answer']