uniq_words_list = []

with open('sentences.txt', 'r') as file:
    for row in file:
        row = row.lower()
        row_words_list = row.split()
        for word_id in range(len(row_words_list)):
            if row_words_list[word_id][-1] == ',':
                row_words_list[word_id] = row_words_list[word_id][:-1:]
            uniq_words_list.append(row_words_list[word_id])
        list(set(uniq_words_list))
        print(row)
        print(row_words_list)
