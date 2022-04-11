import unittest
from io import StringIO

from cat import cat


class MyTestCase(unittest.TestCase):
    def test_something(self):
        input_string = "abc\ndef"
        expected_output = input_string
        source = StringIO(input_string)
        out = StringIO()
        cat(source, out)
        out.seek(0)
        self.assertEqual(expected_output, out.read())


if __name__ == '__main__':
    unittest.main()
