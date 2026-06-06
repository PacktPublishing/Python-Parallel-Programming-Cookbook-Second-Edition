# Defines a Celery task for distributed execution

from celery import Celery

# Configure Celery application and message broker
app = Celery(
    'tasks',
    broker='pyamqp://guest@localhost//'
)

# Task executed by Celery workers
@app.task
def add(x, y):
    return x + y