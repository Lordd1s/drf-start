from celery import shared_task


@shared_task
def your_task():
    # Ваш код для выполнения задачи
    print("Task completed!")
