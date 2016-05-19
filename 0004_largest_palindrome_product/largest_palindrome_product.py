# A palindromic number reads the same both ways.
# Find the largest palindrome made from the product of two 3-digit numbers

largest_three_digit_num = 999

x = largest_three_digit_num

max_palindrome = 0

while x > 99:
    y = largest_three_digit_num
    while y > 99:
        answer = x * y
        # print answer
        if str(answer) == str(answer)[::-1] and answer > max_palindrome:
            print "found palindrome: " + str(answer)
            max_palindrome = answer
        y -= 1
    x -= 1

print max_palindrome
