import unittest
from converter import celsius_to_fahrenheit

class TestConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        # Test 0°C to 32°F
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        # Test 100°C to 212°F
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        # Test -40°C to -40°F
        self.assertEqual(celsius_to_fahrenheit(-40), -40)

if __name__ == '__main__':
    unittest.main()
