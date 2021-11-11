from django.shortcuts import render,redirect,get_object_or_404
from celery.result import AsyncResult
from celeryTest.tasks import add,debug_task
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from .forms import DayCreateForm,NumberCreateForm,NumbergenCreateForm
from .models import Day,Number,Progress
from .do_something import slow_function
import functools
# TaskResultをインポート
from django_celery_results.models import TaskResult

def celery_test(request):

	result = add.delay()  # 非同期処理の呼び出しはこれだけでOK。後は非同期に処理が流れていく

	print("add.delay終了")
	debug_task()

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

def ajax_index(request):
    form = NumberCreateForm(request.POST or None)
    formgen = NumbergenCreateForm(request.POST or None)
    context = {
        "form":form,
        "formgen":formgen,
    }
    return render(request,"testapp/ajax_test.html",context)

def ajax_number(request):
    number1 = int(request.POST.get('number1'))
    number2 = int(request.POST.get('number2'))
    plus = number1 + number2
    minus = number1 - number2
    d = {
        'plus': plus,
        'minus': minus,
    }
    return JsonResponse(d)

#------------------------------------------------------------------------------------------

def setup(request):
    """進捗管理インスタンスを作成する"""
    gen = int(request.POST.get("gen"))
    print("総ステップ数:%s" % gen)
    progress = Progress.objects.create(total=gen)
    return HttpResponse(progress.pk)

def show_progress(request):
    """時間のかかる関数を実行する"""
    if "progress_pk" in request.POST:
        # progress_pkが指定されている場合の処理
        progress_pk = request.POST.get("progress_pk")
        progress = get_object_or_404(Progress, pk=progress_pk)
        persent = str(int(progress.now / progress.total * 100)) + "%"
        print("show_progress実行")
        return render(request, "testapp/progress_bar.html", {"persent": persent})
    else:
        # progress_pkが指定されていない場合の処理
        return HttpResponse("エラー")

def make_progress(pk):
    """引数のプライマリーキーに紐づく進捗を進める"""
    progress = get_object_or_404(Progress, pk=pk)
    progress.now += 1
    progress.save()

def set_hikisuu(pk):
    """引数を固定する"""
    return functools.partial(make_progress, pk=pk)


def do_something(request):
    print("do_something呼び出し")
    """時間のかかる関数を実行する"""
    if "progress_pk" in request.POST:
        # progress_pkが指定されている場合の処理
        progress_pk = request.POST.get("progress_pk")
        number1 = int(request.POST.get("number1"))
        number2 = int(request.POST.get("number2"))
        gen = int(request.POST.get("gen"))
        result = slow_function(number1,number2,gen,set_hikisuu(progress_pk))
        return render(request, "testapp/result.html", {"result": result})
    else:
        # progress_pkが指定されていない場合の処理
        return HttpResponse("エラー")


#------------------------------------------------------------------------------------------

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


