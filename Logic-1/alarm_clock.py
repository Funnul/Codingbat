def alarm_clock(day, vacation):
    weekday = (1 <= day <= 5)
    weekend = (day == 0 or day == 6)
    if vacation and weekend:
        return 'off'
    elif (vacation and weekday) or (weekend):
        return '10:00'
    return '7:00'
