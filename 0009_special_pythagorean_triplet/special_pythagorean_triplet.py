# Knowns
# a + b + c = 1000
# a^2 + b^2 = c^2
# a < 333 and c > 333

import math


def squared(x):
    return x * x

flag = 0
for c in range(333, 999):
    for a in range(1, 333):
        b_diff = 1000 - c - a
        b_squared_potential = squared(c) - squared(a)
        b_potential = math.sqrt(b_squared_potential)
        if(b_potential == b_diff):
            flag = 1
            b = int(round(b_potential, 0))
            break
    if flag == 1:
        break

print a, b, c

print "sum " + str(a + b + c)
print "product " + str(a * b * c)
