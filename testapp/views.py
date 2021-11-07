from django.shortcuts import render,redirect
from celery.result import AsyncResult
from celeryTest.tasks import add
from .forms import DayCreateForm
from .models import Day
# TaskResultをインポート
from django_celery_results.models import TaskResult

def celery_test(request):

	result = add.delay()  # 非同期処理の呼び出しはこれだけでOK。後は非同期に処理が流れていく

	print("add.delay終了")

	task_id = result.id  # 一意に割り振られたIDが確認できる。

	print('task_id:', task_id)

	context = {
			   "ready":result.ready(),
			   'taskid': task_id,
	}

	return render(request, 'testapp/celery_test.html', context)

import os
def boot(request):
	context = {
		"redis": os.environ["REDIS_URL"],
	}
	return render(request,"testapp/index.html",context)

def index(request):
	context = {
        'day_list':Day.objects.all(),
    }
	return render(request,'testapp/day_list.html',context)

def adddiary(request):
    #送信内容を基にフォームをつくる
    form = DayCreateForm(request.POST or None)

    #method=POSTつまり、送信ボタン押下時、入力内容に問題がなければ
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('testapp:index')

    #通常ページのアクセス、入力内容に誤りがある場合、またページを表示
    context = {
        'form':form
    }
    return render(request,'testapp/day_form.html',context)
