# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

number_to_factorize = 600851475143  # 600851475143


def get_potential_factors(number_to_factorize):
    potential_factors = set()
    if number_to_factorize % 2 == 0:
        potential_factors.add(2)

    for potential_factor in \
            xrange(3, int(math.sqrt(number_to_factorize)), 2):
        if number_to_factorize % potential_factor == 0:
            potential_factors.add(potential_factor)

    return potential_factors


potential_factors = get_potential_factors(number_to_factorize)
print potential_factors

actual_factors = set()
for potential_factor in potential_factors:
    flag = 1
    for other_factor in potential_factors:
        if potential_factor != other_factor and \
                potential_factor % other_factor == 0:
            flag = 0
            break
    if flag == 1:
        actual_factors.add(potential_factor)

print actual_factors

max_factor = 0
for actual_factor in actual_factors:
    if actual_factor > max_factor:
        max_factor = actual_factor

print max_factor
