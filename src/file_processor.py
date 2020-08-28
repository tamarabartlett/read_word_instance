import collections
import functools
import string
import operator

def get_dict_of_words(line):
    line_arr = str.split(line, ' ')
    dict_of_words = dict()
    for word in line_arr:
        normalized_word = get_normalized_word(word)
        if normalized_word not in dict_of_words.keys():
            dict_of_words[normalized_word] = 1
        else:
            dict_of_words[normalized_word] += 1
    return dict_of_words


def get_normalized_word(word):
    lower_word = word.lower()
    no_punct = str.maketrans('', '', string.punctuation)
    lower_word_no_punct = lower_word.translate(no_punct)
    return lower_word_no_punct


def merge_dicts(dict_1, dict_2):
    list_dicts = [dict_1, dict_2]
    return functools.reduce(operator.add,
         map(collections.Counter, list_dicts))


def read_file(input):
    input_lines = str.splitlines(input)
    num_input_lines = input_lines[0]
    text_lines = []

    for i in range(int(num_input_lines)+1):
        text_lines.append(input_lines[i+1])
    return text_lines


if __name__ == '__main__':
    nput_string = 'Wait a minute. Wait A minute, Doc'
    get_dict_of_words(nput_string)
