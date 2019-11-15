import numpy as np
import pprint
import re
uniq_words_list_raw = []
all_strings = []
res_freq_list = []


def my_func():
    with open('sentences.txt', 'r') as file:
        for row in file:

            row_words_list = re.split('[^a-z]', row.lower())
            row_words_list = [x for x in row_words_list if x != '']
            all_strings.append(row_words_list)
            print(row_words_list)
            for word in row_words_list:
                if word not in uniq_words_list_raw:
                    uniq_words_list_raw.append(word)
            uniq_words_list = list(set(uniq_words_list_raw))

    for string in all_strings:
        list_for_arr = []
        for word_id in range(len(uniq_words_list)):
            frequency = row_words_list.count(uniq_words_list[word_id])
            list_for_arr.append(frequency)

        res_freq_list.append(list_for_arr)

    matrix = np.array(res_freq_list)
    pprint.pprint(matrix)
    print(matrix.shape)
    print(matrix[0])


if __name__ == '__main__':
    my_func()
