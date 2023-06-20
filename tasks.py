from robocorp.tasks import task

@task
def minimal_task():
    message = "Hello"
    message = message + " World!"
