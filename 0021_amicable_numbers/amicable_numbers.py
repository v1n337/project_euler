
cache = dict()
confirmed_amics = set()
confirmed_non_amics = set()


def find_factors(number):
    midway = number / 2
    factors = set()
    factors.add(1)
    for i in xrange(2, midway + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number / i)
    # print sorted(factors)
    return factors

for i in xrange(1, 10001):
    cache[i] = sum(find_factors(i))

for number in cache:
    potential_amic = cache[number]
    if potential_amic in cache and \
            potential_amic not in confirmed_amics and \
            potential_amic not in confirmed_non_amics and \
            number == cache[potential_amic] and \
            number != potential_amic:
        # print number, " is amicable with", potential_amic
        confirmed_amics.add(number)
        confirmed_amics.add(potential_amic)
    else:
        confirmed_non_amics.add(number)

print sum(confirmed_amics)
