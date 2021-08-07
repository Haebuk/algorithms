import calendar
def solution(a, b):
    weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return weekdays[calendar.weekday(2016, a, b)]
