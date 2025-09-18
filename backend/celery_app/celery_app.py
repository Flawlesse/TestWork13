from celery import Celery


app = Celery("celery_app")
app.config_from_object("celery_app.celeryconfig")
app.autodiscover_tasks(["celery_tasks"], force=True)
