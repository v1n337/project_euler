
all_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
name_scorer_cache = dict()
file_of_names = 'p022_names.txt'


def create_name_scorer_cache():
    score = 1
    for i in all_alphabets:
        name_scorer_cache[i] = score
        score += 1
    # print name_scorer_cache


def read_names_from_file():
    with open(file_of_names, 'r') as f:
        name_list = f.read().split(",")
    return map(lambda x: x[1:len(x) - 1], name_list)


def calculate_name_score(name):
    score = 0
    for char in name:
        score += name_scorer_cache[char]
    return score

create_name_scorer_cache()
sorted_name_list = sorted(read_names_from_file())

name_position = 1
total_score = 0
for name in sorted_name_list:
    # print name
    score = calculate_name_score(name) * name_position
    name_position += 1
    total_score += score
    # break

print total_score
