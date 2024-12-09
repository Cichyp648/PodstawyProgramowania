def time_string(hours, minutes, time_format):
    minute_str = f"{minutes:02d}"
    
    if time_format == '24':
        return f"{hours:02d}:{minute_str}"
    
    elif time_format == '12':
        if hours == 0:
            hour_12 = 12
            am_pm = 'am'
        elif hours > 12:
            hour_12 = hours - 12
            am_pm = 'pm'
        elif hours == 12:
            hour_12 = 12
            am_pm = 'pm'
        else:  # 1 to 11 AM
            hour_12 = hours
            am_pm = 'am'
        
        return f"{hour_12}:{minute_str}{am_pm}"

def test_time():
    print(time_string(15, 38, '24'))
    print(time_string(8, 3, '24'))  
    print(time_string(0, 5, '24'))
    print(time_string(11, 15, '12'))
    print(time_string(0, 7, '12'))
    print(time_string(7, 30, '12'))
    print(time_string(12, 46, '12'))
    print(time_string(13, 10, '12'))
    print(time_string(19, 2, '12'))

test_time()
