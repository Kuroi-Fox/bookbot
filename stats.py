from operator import itemgetter

def word_count(book):
    words_lst = book.split()
    return len(words_lst)


def letter_count(book):
    temp_dict = {}
    for letter in book:
        if letter.isalpha():
            if letter not in temp_dict: 
                temp_dict[letter] = 1
            else:
                temp_dict[letter] += 1
    final_lst = dict_sort(temp_dict)
    return final_lst

def dict_sort(dict):
    new_lst = []
    for item in dict:
        temp_dict = {"char": item, "num": dict[item]}
        new_lst.append(temp_dict)
    sorted_lst = sorted((new_lst), reverse=True, key=itemgetter("num"))
    return sorted_lst

