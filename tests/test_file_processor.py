from unittest import TestCase
from src.file_processor import (
    read_file
)

class FileProcessorTests(TestCase):
    def test_file_returns_self(self):
        input_file = '''2
        Wait a minute. Wait a minute, Doc.
        Are you telling me that you built a time machine out of a DeLorean?'''

        output_file = read_file(input_file)

        self.assertEqual(input_file, output_file)

if __name__ == '__main__':
    unittest.main()
