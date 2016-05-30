import math
import time

start_time = time.time()
lower_barrier = 500


def find_factors(number, midway):
    factors = set()
    for i in xrange(1, midway + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number / i)
    # print sorted(factors)
    return factors


number = 0
counter = 1
while number < lower_barrier:
    number += counter
    counter += 1
    # print number

print "lower_barrier:", number

while True:
    midway = int(math.sqrt(number))
    # print midway
    factors = find_factors(number, midway)
    print number, "has no_of_factors", len(factors)
    print "counter", counter
    if len(factors) > 500:
        print sorted(factors)
        print number, "is what we're looking for."
        break
    # exit(0)

    number += counter
    counter += 1

end_time = time.time()

print "time taken", (end_time - start_time)
