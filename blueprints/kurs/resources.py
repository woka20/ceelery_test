  # TaskBase=celery.Task
    # class ContextTask(TaskBase):
    #     abstract=True
    #     def __call__(self,*args,**kwargs):
    #         with app.app_context():
    #                return TaskBase.__call__(self, *args, **kwargs)
    # celery.Task=ContextTask




# celery.conf.beat_schedule={
#     'every-10-sec':{
#         'task':'tasks.req_url',
#         'schedule':10.0
#     }
# }