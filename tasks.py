import requests
from flask import Flask
from blueprints.show import flask_celery
import datetime

app=Flask(__name__)
app.config['CELERY_BROKER_URL']='amqp://localhost'

# celery = Celery('tasks', broker=app.config['CELERY_BROKER_URL'])
celery=flask_celery.make_celery(app)
celery.conf.update(app.config)

@app.route('/')
def show():
    result=req_url.delay()

    return  "OKE"

@celery.task(name="tasks.req_url")
def req_url():
    r=requests.get('https://api.exchangeratesapi.io/latest?base=IDR')
    return r.text

if __name__=='__main__':
    app.run(debug=True)