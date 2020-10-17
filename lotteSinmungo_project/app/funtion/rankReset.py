# from datetime import datetime, timedelta
# from apscheduler.schedulers.blocking import BlockingScheduler
# from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
# from ..models import Problem
# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore(), "default")
# @register_job(scheduler, "interval", seconds=3600)
# def delete_post():
#     for record in Problem.objects.all():
#         time_elapsed = datetime.now() - record.updated_at
#         if time_elapsed > timedelta(hours=1):
#            record.delete()
# register_events(scheduler)