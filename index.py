def add_time(time, duration, date=''):
    # Split start time
    time_parts = time.split()
    hour_min = time_parts[0].split(':')
    am_pm = time_parts[1]

    start_hour = int(hour_min[0])
    start_minute = int(hour_min[1])

    if am_pm == 'PM' and start_hour != 12:
        start_hour += 12
    elif am_pm == 'AM' and start_hour == 12:
        start_hour = 0

    dur_hour, dur_minute = map(int, duration.split(':'))

    total_minutes = start_minute + dur_minute
    extra_hour = total_minutes // 60
    final_minutes = total_minutes % 60

    total_hours = start_hour + dur_hour + extra_hour
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24

    if final_hour_24 == 0:
        final_hour = 12
        period = 'AM'
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        period = 'AM'
    elif final_hour_24 == 12:
        final_hour = 12
        period = 'PM'
    else:
        final_hour = final_hour_24 - 12
        period = 'PM'

    # Weekday calculation
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    final_day = ''
    
    if date:
        index = week.index(date.capitalize())
        final_day = week[(index + days_later) % 7]

    if days_later == 1:
        day_note = ' (next day)'
    elif days_later > 1:
        day_note = f' ({days_later} days later)'
    else:
        day_note = ''

    if final_day:
        result = f'{final_hour}:{str(final_minutes).zfill(2)} {period}, {final_day}{day_note}'
    else:
        result = f'{final_hour}:{str(final_minutes).zfill(2)} {period}{day_note}'

    print(result)
    return result

