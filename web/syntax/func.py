a=1
b=2
c=3
s=a+b+c
r=s/3
print(r)

def average():
    a=1
    b=2
    c=3
    s=a+b+c
    r=s/3
    print(r)


average()

# parameter 매개변수
def average(a, b, c):
    s=a+b+c
    r=s/3
    print(r)

# argument 인자
average(10, 20, 30)



def average(a, b, c):
    s=a+b+c
    r=s/3
    return r

print(average(10, 20, 30))
