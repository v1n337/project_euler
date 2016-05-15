value_limit = 4000000

old_number = 0
current_number = 1
sum_numbers = 0

while current_number < value_limit:
    addition = current_number + old_number
    old_number = current_number
    current_number = addition

    if current_number % 2 == 0:
        # print "current_number: " + str(current_number)
        sum_numbers += current_number

print sum_numbers
