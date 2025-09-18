from celery import Celery


app = Celery("backend")
app.config_from_object("celeryconfig")

# we need to do that in order to actually run the modules
# where the tasks are registered
import backend.celery_tasks.tasks as tasks  # NOQA
