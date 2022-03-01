import datetime
from datetime import timedelta
x = datetime.datetime.now()
five_days = timedelta(5)
five_days_ago = x - five_days
print(five_days_ago.strftime("%A"))