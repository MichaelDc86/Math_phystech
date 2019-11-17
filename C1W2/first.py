import numpy as np
from scipy.spatial import distance
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

            for word in row_words_list:
                if word not in uniq_words_list_raw:
                    uniq_words_list_raw.append(word)

    for string in all_strings:
        list_for_arr = []
        for word_id in range(len(uniq_words_list_raw)):
            frequency = string.count(uniq_words_list_raw[word_id])
            list_for_arr.append(frequency)

        res_freq_list.append(list_for_arr)

    matrix = np.array(res_freq_list)
    pprint.pprint(matrix)
    print(matrix.shape)
    # print(matrix[0])
    # print(len(matrix))

    cos_distance_arr = []
    for i in range(1, len(matrix)):
        cos_distance_tmp = distance.cosine(matrix[0], matrix[i])
        cos_distance_arr.append(cos_distance_tmp)
    print(cos_distance_arr)
    first_min = min(cos_distance_arr)
    first_min_index = cos_distance_arr.index(first_min)
    cos_distance_arr[first_min_index] = 1
    second_min = min(cos_distance_arr)
    second_min_index = cos_distance_arr.index(second_min)
    print(first_min_index)
    print(second_min_index)


if __name__ == '__main__':
    my_func()
