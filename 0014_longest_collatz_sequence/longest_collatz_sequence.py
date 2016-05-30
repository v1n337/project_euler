import time

max_chain_length = -1
starting_number = 0
number_cache = dict()
start_time = time.time()

def generate_collatz_chain(number):
    collatz_chain = [number]
    while number != 1:
        if number in number_cache:
            existing_chain = number_cache.get(number)
            collatz_chain.extend(existing_chain)
            break
        if number % 2 == 0:
            number /= 2
        else:
            number = (3 * number) + 1
        collatz_chain.append(number)
        # print collatz_chain
    number_cache[number] = collatz_chain
    return collatz_chain

for i in xrange(1, 1000000):
    collatz_chain = generate_collatz_chain(i)
    # print "for", i, "the collatz chain is", collatz_chain
    if len(collatz_chain) > max_chain_length:
        max_chain_length = len(collatz_chain)
        starting_number = i

print "starting_number", starting_number
print "max_chain_length", max_chain_length
print "it took ", (time.time() - start_time), "seconds"
