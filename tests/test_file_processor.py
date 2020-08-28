from unittest import TestCase
from src.file_processor import (
    get_dict_of_words,
    get_normalized_word,
    merge_dicts,
    read_file
)

class FileProcessorTests(TestCase):
    def test_file_returns_self(self):
        input_file = '''2
Wait a minute. Wait a minute, Doc.
Are you telling me that you built
a time machine out of a DeLorean?'''

        output_array = read_file(input_file)
        expected_array = ['Wait a minute. Wait a minute, Doc.', 'Are you telling me that you built', 'a time machine out of a DeLorean?']

        self.assertEqual(len(output_array), 3)
        self.assertEqual(output_array, expected_array)

    def test_merge_dicts(self):
        dict_1 = {'wait':2, 'a': 2, 'minute': 2, 'doc': 1}
        dict_2 = {'are':2, 'you': 2, 'telling': 2, 'doc': 3, 'a': 2}
        expected_dict = {'wait':2 , 'a': 4, 'minute': 2, 'doc': 4, 'are':2, 'you': 2, 'telling': 2}
        merged_dict = merge_dicts(dict_1, dict_2)
        self.assertEqual(expected_dict, merged_dict)

    def test_words_into_dict(self):
        input_string = 'Wait a minute. Wait A minute, Doc'
        expected_dict = {'wait':2, 'a': 2, 'minute': 2, 'doc': 1}
        output = get_dict_of_words(input_string)
        self.assertEqual(expected_dict, output)

    def test_get_plain_word(self):
        self.assertEqual(get_normalized_word('Word.'), 'word')

if __name__ == '__main__':
    unittest.main()
