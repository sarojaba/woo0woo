import csv
import re

# https://github.com/korean-word-game/db
f = open("kr_korean.csv", "r")
try:
    reader = csv.reader(f, delimiter=",")

    lines = [line[1] for line in enumerate(reader)]

    lines_noun = list(filter(lambda l: l[1].endswith('명사'), lines))

    words_noun = [l[0] for l in lines_noun]

    words_pure = [re.sub("[-^]", "", w) for w in words_noun]

    words_len_3 = list(filter(lambda w: len(w) == 3, words_pure))

    words_palindrome = list(filter(lambda w: w[0] == w[2], words_len_3))

    words_not_same_all = list(filter(lambda w: w[0] != w[1], words_palindrome))

    words_unique = list(set(words_not_same_all))

    # Prevent broken characters
    words_only_korean = list(filter(lambda w: re.fullmatch("[\u3130-\u318F\uAC00-\uD7A3]{3}", w), words_unique))

    words_sorted = sorted(words_only_korean)

    for i, w in enumerate(words_sorted):
        print("'" + w + "',")
finally:
    f.close()
