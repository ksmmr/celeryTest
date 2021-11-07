from django.shortcuts import render
from celery.result import AsyncResult

from celeryTest.tasks import add

def celery_test(request):
	task_id = add.delay(5, 5)

	result = AsyncResult(task_id)
	print('result:', result, ' : ', result.state, ' : ', result.ready())

	context = {'result': result}

	return render(request, 'testapp/celery_test.html', context)

def boot(request):
	return render(request,"testapp/index.html")