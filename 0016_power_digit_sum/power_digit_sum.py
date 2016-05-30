
number = 2 ** 1000
# print "number", number

summation = 0
while number >= 10:
    summation += number % 10
    number = number / 10

summation += number % 10

print summation
