from __future__ import absolute_import
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from main.models import Quiz, Question
from main.utils import get_answer
logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="adding_answers",
    ignore_result=True
)
def adding_answers():
    questions = Question.objects.all()

    for question in questions:
        if not question.quiz.canPublish:
            # do magic
            answer = get_answer(question.question_description)
            question.answer = answer
            question.quiz.canPublish = True
            question.save()
            question.quiz.save()
            logger.info(" Brace yourself " + question.question_description + "is getting answered")
    return "answered question {}".format(question.question_description)
