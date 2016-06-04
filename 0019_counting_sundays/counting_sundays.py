from datetime import datetime, timedelta

start_date_str = '1901-01-01'
end_date_str = '2000-12-31'

start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

# print start_date.date(), end_date.date()
# print start_date.date().weekday(), end_date.date().weekday()
# print start_date.date().day, end_date.date().day

count = 0
current_date = start_date.date()
while current_date <= end_date.date():
    if current_date.day == 1 and current_date.weekday() == 6:
        count += 1
    current_date += timedelta(days=1)

print "count:", count
