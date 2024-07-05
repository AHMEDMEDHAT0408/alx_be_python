import datetime

def display_current_datetime():
    current_date_time = datetime.datetime.now()
    formatted_current_date_time = current_date_time.date()
    print(f"Current date and time: {formatted_current_date_time}")

def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.datetime.now().date()
    future_date = current_date + datetime.timedelta(days=days)
    formatted_future_date = future_date
    print(f"Future date: {formatted_future_date}")


