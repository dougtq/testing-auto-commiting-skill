import unittest
from unittest.mock import patch
import io
import sys

# We'll test the main function of main.py
from main import main

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '0'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_temperature_conversion(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("32.0", output)
        self.assertIn("Fahrenheit", output)

    @patch('builtins.input', side_effect=['2', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_distance_conversion(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("0.621371", output)
        self.assertIn("miles", output)

if __name__ == '__main__':
    unittest.main()
