
charmap = {
    "0": ("", "", "ten"),
    "1": ("one", "", "eleven"),
    "2": ("two", "twenty", "twelve"),
    "3": ("three", "thirty", "thirteen"),
    "4": ("four", "forty", "fourteen"),
    "5": ("five", "fifty", "fifteen"),
    "6": ("six", "sixty", "sixteen"),
    "7": ("seven", "seventy", "seventeen"),
    "8": ("eight", "eighty", "eighteen"),
    "9": ("nine", "ninety", "nineteen")
}


def get_relevant_word(digit, position_of_digit, overall_length):
    # print "checking - digit", digit, "position_of_digit", position_of_digit
    if position_of_digit == 2:
        return_value = ""
        if digit[0] == "1":
            (standalone, tens, teens) = charmap.get(digit[1])
            return_value = teens
        elif digit[0] == "0":
            (standalone, tens, teens) = charmap.get(digit[1])
            return_value = standalone
        else:
            (x, tens, y) = charmap.get(digit[0])
            (standalone, x, y) = charmap.get(digit[1])
            return_value = tens + standalone

        if overall_length > 2:
            if return_value == "":
                return ""
            else:
                return "and" + return_value
        else:
            return return_value

    (standalone, tens, teens) = charmap.get(digit)
    if position_of_digit == 4:
        return standalone + "thousand"
    elif position_of_digit == 3:
        return standalone + "hundred" if (digit != "0") else ""
    else:
        return standalone


def convert_number_to_text(number):
    word = ""
    numstr = str(number)
    overall_length = len(numstr)

    if overall_length == 1:
        return get_relevant_word(numstr[0], 1, overall_length)

    while len(numstr) > 1:
        length = len(numstr)
        if length == 2:
            word += get_relevant_word(numstr[0:2], length, overall_length)
        else:
            word += get_relevant_word(numstr[0], length, overall_length)
        numstr = numstr[1:]

    return word


overall_sum = 0
for i in xrange(1, 1001):
    text = convert_number_to_text(i)
    text_len = len(text)
    overall_sum += text_len
    print text, text_len

print overall_sum
# print convert_number_to_text(15)
