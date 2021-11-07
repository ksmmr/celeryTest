from django.shortcuts import render
from celery.result import AsyncResult
from celeryTest.tasks import add
# TaskResultをインポート
from django_celery_results.models import TaskResult



def celery_test(request):

	result = add.delay(5, 5)  # 非同期処理の呼び出しはこれだけでOK。後は非同期に処理が流れていく

	print("===============")

	task_id = result.id  # 一意に割り振られたIDが確認できる。

	print('task_id:', task_id)

	context = {"result":result.get(),
			   "ready":result.ready(),
			   'taskid': task_id}

	return render(request, 'testapp/celery_test.html', context)

import os
def boot(request):
	context = {
		"redis": os.environ["REDIS_URL"],
	}
	return render(request,"testapp/index.html",context)