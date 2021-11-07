from django.shortcuts import render
from celery.result import AsyncResult
from celeryTest.tasks import add
# TaskResultをインポート
from django_celery_results.models import TaskResult



def celery_test(request):

	task_id = add.delay(5, 5)

	result = AsyncResult(task_id)
	print('result:', result)

	# TaskResultオブジェクトから実行結果を取得
	result_object = TaskResult.objects.get(task_id=task_id)

	context = {'result': result,
			   "result_object":result_object}

	return render(request, 'testapp/celery_test.html', context)

import os
def boot(request):
	context = {
		"redis": os.environ["REDIS_URL"],
	}
	return render(request,"testapp/index.html",context)