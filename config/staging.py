import os
from datetime import timedelta

DEBUG = True
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
SECRET_KEY="\x1d\x02\xfbq\xb5tz\xae\x01\xbf?4\xe4\xb4\x80A\xa7\xd0\xcbRX\xd5\x00\xda"
# CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERYBEAT_SCHEDULE = {
#     'example_task': {
#         'task': 'tasks.example_task',
#         'schedule': timedelta(minutes=2),
#         'args': ()
#     },
# }

ERROR_404_HELP = False
