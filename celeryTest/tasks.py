from celery import shared_task
import time

@shared_task
def add():
	print("add関数が呼び出された")
	time.sleep(10)
	y = 10 + 10
	print('add関数処理完了')
	return y