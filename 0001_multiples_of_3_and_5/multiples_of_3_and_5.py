input_numbers = range(1, 1000)

sum = 0
for number in input_numbers:
    if number % 3 == 0:
        sum += number
    elif number % 5 == 0:
        sum += number

print sum
