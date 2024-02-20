import datetime

#task1
five_days_ago = datetime.datetime.now()
print(five_days_ago.year, five_days_ago.month, five_days_ago.day - 5, five_days_ago.strftime("%A"))

#OR

current_date = datetime.date.today()
five_days_ago = datetime.timedelta(days=5)
result_date = current_date - five_days_ago

print("Current Date:", current_date)
print("Five Days Ago:", result_date)
#task2

today = datetime.date.today()
one_day = datetime.timedelta(days=1)
print(f"Yestrday: {today - one_day};\nToday: {today};\nTommorow: {today + one_day};")

#task3
with_microseconds = datetime.datetime(2024, 2, 19, 15, 30, 20, 500)
without_microseconds = with_microseconds.replace(microsecond=0)
print("Original DateTime:", without_microseconds)
print("DateTime without Microseconds:", without_microseconds)

#task4

one_date = datetime.datetime(2024, 2, 19, 15, 30, 20)
second_date = datetime.datetime(2024, 2, 19, 15, 30, 10)
print(one_date.second - second_date.second)