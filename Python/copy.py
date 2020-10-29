# 1. list

ll = [10, 30, 20, 13]

def change(l):
    l[0] = 100

change(ll)

print(ll)
# list could be changed, for list deliver address
# [100, 30, 20, 13]

# 2. not list

xx = 555

def change_value(x):
    x += 111

change_value(xx)
print(xx)
# the value could not be changed, for in function local variable can't effect on global variable,
# xx copy and deliver the value
# 555







