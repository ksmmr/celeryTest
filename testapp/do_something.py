import time
from celery import shared_task

@shared_task
def slow_function(number1,number2,gen,make_progress_func):
    plus = 0
    minus = 0
    for i in range(gen):
        time.sleep(0.1)
        plus += number1+number2
        minus += number1-number2

        make_progress_func()


    return plus,minus