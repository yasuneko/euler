import random
import math

def answer(x):
    total = 0
    three = 1
    three_list = []
    while total < x:
        total += three
        three_list.append(three)
        three = three * 3

    tmp = x
    left = []
    right = []
    output = []
    while three_list:
        a = three_list.pop()
        if abs(abs(tmp) - a) > abs(tmp):
            output.append('-')
        elif tmp > 0:
            tmp = tmp - a
            right.append(a)
            output.append('R')
        elif tmp < 0:
            tmp = tmp + a
            left.append(a)
            output.append('L')
    #print x, '= [', str(x), ']', ','.join([str(l) for l in left]), '|', ','.join([str(r) for r in right])
    return list(reversed(output))

#print answer(1000000000)

print answer(27)

exit()

for i in range(1,100000):
    if answer(i) == False:
        print i

#for i in range(0, 10):
#    x = random.randint(1,1000000000)
#    answer(x)

#answer(3)
#answer(13)
#answer(15)
#answer(27)
