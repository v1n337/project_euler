
max_number = 2000000
primes = [2]
non_primes = set([1])
number = 3
count = 1


def insert_non_primes(number):
    i = 2
    non_prime_number = 1
    while non_prime_number < max_number:
        non_prime_number = i * number
        non_primes.add(non_prime_number)
        i += 1
    # print list(non_primes)


def is_prime(number, primes):
    if number in non_primes:
        return False
    for prime in primes:
        if number % prime == 0:
            return False
    insert_non_primes(number)
    return True


while number < max_number:
    if is_prime(number, primes):
        # print number
        primes.append(number)
    number += 2

# print primes
print "length: " + str(len(primes))
print "sum: " + str(sum(primes))
