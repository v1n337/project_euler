
sum_of_squares = 0


def squared(x):
    return x * x

sum_of_numbers = 0
for number in xrange(1, 101):
    sum_of_squares += squared(number)
    sum_of_numbers += number

square_of_sum = squared(sum_of_numbers)
print "sum_of_squares " + str(sum_of_squares)
print "square_of_sum " + str(square_of_sum)

print "difference " + str(abs(square_of_sum - sum_of_squares))
