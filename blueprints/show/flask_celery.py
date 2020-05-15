from celery import Celery
from blueprints.show import celeryconfig

def make_celery(app):
    celery=Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])

    # celery.conf.update(app.config)
    celery.config_from_object(celeryconfig)

    return celery
                  