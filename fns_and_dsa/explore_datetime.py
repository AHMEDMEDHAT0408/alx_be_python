import datetime
date_now = datetime.datetime.now()
print(f"Current date and time: {date_now}")
days = int(input("Enter the number of days to add to the current date: "))
future_date = date_now + datetime.timedelta(days=days)
future_date_only_date = future_date.date()
print(f"Future date: {future_date_only_date}")