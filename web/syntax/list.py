squares = [1, 'four', 9, 16, 25]
print(squares)
print(squares[3])
print(len(squares))
squares[1] = 4
print(squares)
del squares[2]
print(squares)
squares.append('minjung')
print(squares)

test = [3, 1, 4, 3]
test = set(test)
print(test)
for i in test:
    print(i)

dct = {'name':'doci', 'num':1}
for i in dct:
    print(i)

test2 = [5, 6, 4, 1]
test2 = tuple(test2)
for i in test2:
    print(i)
