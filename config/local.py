from datetime import timedelta

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/dogear'
# SQLALCHEMY_ECHO = True
CELERY_BROKER_URL = 'sqla+postgresql://localhost/dogear'
CELERY_TASK_SERIALIZER = 'json'
OAUTHLIB_INSECURE_TRANSPORT=1
SECRET_KEY="\x1d\x02\xfbq\xb5tz\xae\x01\xbf?4\xe4\xb4\x80A\xa7\xd0\xcbRX\xd5\x00\xda"
CELERY_ACCEPT_CONTENT = ['json']
CELERYBEAT_SCHEDULE = {
    'example_task': {
        'task': 'tasks.example_task',
        'schedule': timedelta(seconds=10),
        'args': ()
    },
}


ERROR_404_HELP = False
