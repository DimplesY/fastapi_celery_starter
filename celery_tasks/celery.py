from celery import Celery

app = Celery(
    "celery_tasks",
    backend="rpc://",
    broker="amqp://guest:guest@rabbitmq:5672//",
    include=["celery_tasks.task_01"],
)

app.conf.timezone = "Asia/Shanghai"
app.conf.enable_utc = False
app.conf.beat_schedule = {
    "add-every-10-seconds": {
        "task": "celery_tasks.task_01.add",
        "schedule": 10.0,
        "args": (16, 16),
    },
}
