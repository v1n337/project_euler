
import time

start_time = time.time()
limit = 28123
abundant_numbers = set()


def find_factors(number):
    factors = set()
    midway = number / 2
    factors.add(1)
    for i in xrange(2, midway + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number / i)
    # print sorted(factors)
    return factors


def is_abundant(number):
    factors = find_factors(number)
    # print number, factors, sum(factors)
    if sum(factors) > number:
        return True
    return False


for i in xrange(12, limit - 11):
    if is_abundant(i):
        abundant_numbers.add(i)

print len(abundant_numbers)
# print sorted(abundant_numbers)

sum_combos = set()
for number_1 in abundant_numbers:
    for number_2 in abundant_numbers:
        sum_combos.add(number_1 + number_2)

print len(sum_combos)
# print sorted(sum_combos)

non_expressable = set()
for i in xrange(1, limit + 1):
    if i not in sum_combos:
        non_expressable.add(i)

print len(non_expressable)
print sum(non_expressable)

print "it took", time.time() - start_time, "seconds"
