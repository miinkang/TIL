# binary_operation.py

'''
<Question>
섬으로 향하라!

'   + -- + - + -   '
'   + --- + - +   '
'   + -- + - + -   '
'   + - + - + - +   '

해(1)와 달(0),
Code의 세상 안으로!(En-Coding)
출력 : 문자열
'''


text =  ['   + -- + - + -   ',
'   + --- + - +   ',
'   + -- + - + -   ',
'   + - + - + - +   ']


a_list = []
for i in text:
    print(i.strip().replace(' ', ''))   # delimiter every space
    print(i.strip().replace(' ', '').replace('+', 1).replace('-'), 0)  # error : replace() argument 2 must be str, not int
    print(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'))
    print(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)) # convert str to binary
    print(chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2))) # convert ascii to chr
    # chr(), ord() : ascii <-> chr
    a_list.append((chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)))) # make a list

join_list = ''.join(a_list)
print(type(join_list))

''' convert list comprehension'''

print(''.join([(chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2))) for i in text]))

''' comprehension exercise '''

# multiplication table

print('\n'.join([f'{i} x {j} = {i*j}' for i in range(2, 10) for j in range(1, 10)]))

''' use function & map '''

msg = [i.strip().replace(' ', '').replace('+', '1').replace('-', '0') for i in text]
print(msg)
print(type(msg))   # <class 'list'>

print(list(map(lambda x : chr(int(x, 2)), msg)))


def f(x):
    return chr(int(x, 2))

print(''.join(list(map(f, msg))))


'''
<solution>

1. delimiter space 
2. convert to 1, 0
3. convert to binary
4. convert ascii to characters 
5. make string 

'''
