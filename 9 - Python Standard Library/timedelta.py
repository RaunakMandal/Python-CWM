from datetime import datetime, timedelta

dt1 = datetime(2020, 8, 3) + timedelta(days=1, seconds=15)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("microseconds", duration.microseconds)
print("total seconds", duration.total_seconds())
