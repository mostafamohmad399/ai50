import datetime
minute_late = None
while True:
    current_time = datetime.datetime.now()
    minute = current_time.minute

    if minute != minute_late:
        print(minute)
        minute_late = minute

#
