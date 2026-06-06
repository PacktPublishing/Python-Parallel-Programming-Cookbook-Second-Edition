# Submits a Celery task asynchronously

from addTask import add

if __name__ == '__main__':

    # Queue task for background execution
    add.delay(5, 5)