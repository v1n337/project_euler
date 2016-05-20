
def is_prime(number, primes):
    for prime in primes:
        if number % prime == 0:
            return False
    return True


primes = [2]
number = 3
count = 1

to_print = 0
while True:
    if is_prime(number, primes):
        primes.append(number)
        count += 1
    if count == 10001:
        to_print = number
        break
    number += 1

# print primes
print to_print
