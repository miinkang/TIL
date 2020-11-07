'''
<question> calculate the date when they get on a boat

now data = 2020.01.01 (YYYY.MM.DD)
waiting_person = 14000605
they are 2 people
they should get on a boat together

available number : 25 on time, 15 on every 10 minutes
available time : everyday 9:00- before 21:00(not include 21:00)

days of every month are different
1 : 1024 days
2 : 512 days
3 : 256 days
4 : 128 days
5 : 64 days
6 : 32 days
7 : 16 days
8 : 8 days
9 : 4 days
10 : 2 days
there is not 11, 12
'''

# available number of a day
# 하루 탑승 가능 수
available_num_hour = 15 * 5 + 25
print(available_num_hour)  # 100
available_num_day = available_num_hour * 12 # 1200

waiting = 14000605

days_geton_everyone = waiting//available_num_day
print(days_geton_everyone)   # 11667

# days of a year
# 2 + 2^1 + 2^2 + ... + 2^10

days = sum([2**i for i in range(10, 0, -1)])
print(days) # 2046

# calculate year
years_geton_everyone = days_geton_everyone//days
print(years_geton_everyone) # 5

# calculate month and day
surdays = days_geton_everyone % days
print(surdays) # 1437

acc = 0
month = 0
for i in range(10, 0, -1):
    day = acc
    acc += 2 ** i
    month += 1
    if acc > surdays:
        break

print(month) # 2

# 2nd month, can get on a boat!
# 2월에 탑승할 수 있다.

print(day) # 1024
dday = surdays - day
print(dday) # 413

# 2nd month 413th day, can get on a boat!

# calculate time

sur_num = waiting % available_num_day
print(sur_num) # 205

# start 9 am, add 9
departure_hour = sur_num // available_num_hour + 9
print(departure_hour) # 11

# depart 11 am

print(sur_num % available_num_hour) # 5

av_min = [25, 40, 55, 70, 85, 100]
sur_num_min = sur_num % available_num_hour
for i in av_min:

    # they(2 people) should get on together
    if sur_num_min + 1 < i:
        dep_min = av_min.index(i) * 10
        break

print(dep_min)

import datetime

today = datetime.datetime.today()
print(today.minute)

# 시간을 표기하는 법
시간 = 19
분 = 1

print(f'{시간:0>2}, {분:0>2}')

print('1'.zfill(2))



# make function

today = datetime.datetime.today()
waiting = 14000605

def solution(waiting):
    days = sum([2 ** i for i in range(10, 0, -1)])
    yy = (waiting // 1200) // days
    surdays = (waiting // 1200) % days

    acc = 0
    mm = 0
    for i in range(10, 0, -1):
        day = acc
        acc += 2 ** i
        mm += 1
        if acc > surdays:
            break

    dd = surdays - day

    sur_num = waiting % available_num_day
    h = sur_num // available_num_hour + 9

    av_min = [25, 40, 55, 70, 85, 100]
    sur_num_min = sur_num % 100
    for i in av_min:
        if sur_num_min + 1 < i:
            m = av_min.index(i) * 10
            break

    if (sur_num + 1 == 99):
        h += 1
        m = 0

    if (m + today.minute > 60):
        h += 1
        m -= 60

    print(yy, mm, dd, h, m)

    return f'departure : {yy+2020}y {mm}m {dd}d {h}h {m}m'


print(solution(waiting))