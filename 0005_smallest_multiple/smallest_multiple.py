# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?


def get_gcd(a, b):
    return a if (b == 0) else get_gcd(b, a % b)


def get_lcm(a, b):
    return a * b / get_gcd(a, b)

# print get_lcm(31, 17)
lcm = 1
for number in xrange(1, 21):
    lcm = get_lcm(number, lcm)

print lcm
