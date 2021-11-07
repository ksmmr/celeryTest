from django.shortcuts import render
from django_celery_results.models import TaskResult

from celeryTest.tasks import add

def celery_test(request):
	"""
	task_id = add.delay(5, 5)

	result = AsyncResult(task_id)
	print('result:', result, ' : ', result.state, ' : ', result.ready())

	context = {'result': result}
	"""
	add.delay(1, 1)
	object_list = TaskResult.objects.all().order_by('pk')
	context = {'object_list': object_list}

	return render(request, 'testapp/celery_test.html', context)

def boot(request):
	return render(request,"testapp/index.html")