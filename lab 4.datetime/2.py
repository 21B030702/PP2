import datetime
from datetime import timedelta
today = datetime.datetime.now()
delta = timedelta(1)
tomorrow = today + delta
yesterday = today - delta
print(yesterday)
print(today)
print(tomorrow)