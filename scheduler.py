from apscheduler.schedulers.background import BackgroundScheduler
from attendance import mark_attendance

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(mark_attendance, 'cron', hour=9, minute=20, args=["lab1", 1])
    scheduler.add_job(mark_attendance, 'cron', hour=10, minute=20, args=["lab1", 2])
    scheduler.start()
