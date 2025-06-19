def add_time(time, duration):

    time_collen = time.replace(' ', '').find(':')
    duration_collen = duration.find(':')
    if time[time_collen + 4:] == 'PM':
        format_collen = time.find('P') 
    else:
        format_collen = time.find('A')


    left_time = time[:time_collen]
    left_duration = duration[:duration_collen]
    right_time = time[time_collen + 1:format_collen]
    right_duration = duration[duration_collen + 1:]

    total_hours = int(left_time) + int(left_duration)
    total_minutes = int(right_time) + int(right_duration)
    # global day, formatd
    if total_hours > 12:
        total_hours = total_hours - 12
        if time[time_collen + 4:] == 'PM':
            day = '(next day)'
            formatd = 'AM'
        else:
            formatd = 'PM'
            day = 'next day'
        


    if total_minutes > 60:
        remainder = total_minutes // 60
        total_minutes = total_minutes - 60
        total_hours += remainder
        
    print(f'{total_hours}:{total_minutes} {formatd} {day}')



add_time('3:00 PM', '23:10')