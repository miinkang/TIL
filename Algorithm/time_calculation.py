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
available_num_hour = 15 * 5 + 25
print(available_num_hour)  # 100
available_num_day = available_num_hour * 12

waiting_num = 14000605

days_geton_everyone = waiting_num//available_num_day
print(days_geton_everyone)   # 11667

# days of a year
# 2 + 2^1 + 2^2 + ... + 2^10

days = sum([2**i for i in range(1, 11)])
print(days) # 2046

# calculate year
years_geton_everyone = days_geton_everyone//days
print(years_geton_everyone) # 5.702346041055718

# calculate days
surdays = days_geton_everyone % days
print(surdays) # 1437

for i in range(1, 11):
    mul = 2 ** i
    surdays = surdays / mul
    print(i, surdays)
    print(i, mul)





