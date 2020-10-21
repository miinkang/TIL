# pabi_PythonProgramming_Week5_repetition

'''
문제 :  정수 안의 각 자리수의 합을 계산하세요.
ex) 1234 -> 1+2+3+4
'''

number = int(input("Input number"))
sum = 0

# --------------------------------- #

for n in str(number):
    n = int(n)
    sum += n

print("각 자리수의 합은 %d입니다." %sum)

# --------------------------------- #

while number > 0:
    digit = number % 10
    print(digit)
    sum += digit
    number = number // 10

print("각 자리수의 합은 %d입니다." %sum)












