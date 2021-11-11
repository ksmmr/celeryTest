import time
from celery import shared_task
from .models import Progress
from django.shortcuts import get_object_or_404

@shared_task
def slow_function(number1,number2,gen,pk):
    plus = 0
    minus = 0
    for i in range(gen):
        time.sleep(0.1)
        plus += number1+number2
        minus += number1-number2

        make_progress(pk)


    return plus,minus

def make_progress(pk):
    """引数のプライマリーキーに紐づく進捗を進める"""
    progress = get_object_or_404(Progress, pk=pk)
    progress.now += 1
    progress.save()