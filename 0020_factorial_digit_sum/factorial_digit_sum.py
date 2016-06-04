
def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number - 1)

number = 100
num_fact = factorial(number)

summation = 0
for i in str(num_fact):
    summation += int(i)

print summation
