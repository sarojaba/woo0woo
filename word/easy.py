import csv
import re

# https://www.korean.go.kr/front/etcData/etcDataView.do?mn_id=46&etc_seq=71
f = open("easy.csv", "r")
try:
    reader = csv.reader(f, delimiter="\t")

    words = [line[1][0] for line in enumerate(reader)]

    words_removesuffix = [re.sub("[0-9]", "", w) for w in words]

    words_len_3 = list(filter(lambda w: len(w) == 3, words_removesuffix))

    words_palindrome = list(filter(lambda w: w[0] == w[2], words_len_3))

    words_unique = list(set(words_palindrome))

    for i, w in enumerate(words_unique):
        print(w)

finally:
    f.close()
