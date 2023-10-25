import string

FILE_NAME = "text_1_var_29"

with open(FILE_NAME) as file:
    lines = file.readlines()

word_stat = dict()

for line in lines:
    formatted = ''.join(map(lambda x: " " if x in string.punctuation else x, line)).strip()
    words = formatted.split(" ")

    for word in words:
        if word in word_stat:
            word_stat[word] += 1
        else:
            word_stat[word] = 1

word_stat = dict(sorted(word_stat.items(), reverse=True, key=lambda item: item[1]))

with open('r_text_1.txt', 'w') as result:
    for key, value in word_stat.items():
        result.write(key + ":" + str(value) + "\n")