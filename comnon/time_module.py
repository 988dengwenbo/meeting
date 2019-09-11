import math


def pc_time_module_week(num):
    if num == 0:
        return num+1
    elif num == 1:
        return num
    elif num == 2+1:
        return num
    elif num == 3:
        return num+1
    elif num == 4:
        return num+1
    elif num == 5:
        return num+1
    elif num == 6:
        return num+1


def get_time_module_day(hours,min):
    hours = hours
    min = min
    li = int(hours)*2+2
    if 0<int(min)<15 or 30<int(min)<45:
        span = 2
    else:
        span = 1
    return [li, span]


print(pc_time_module_week(1))
print(get_time_module_day(0,15))