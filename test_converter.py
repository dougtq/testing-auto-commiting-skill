import unittest
from converter import celsius_to_fahrenheit, km_to_miles

class TestConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        # Test 0°C to 32°F
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        # Test 100°C to 212°F
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        # Test -40°C to -40°F
        self.assertEqual(celsius_to_fahrenheit(-40), -40)

    def test_km_to_miles(self):
        # Test 1 km to ~0.621371 miles
        self.assertAlmostEqual(km_to_miles(1), 0.621371, places=6)
        # Test 100 km to ~62.1371 miles
        self.assertAlmostEqual(km_to_miles(100), 62.1371, places=4)
        # Test 0 km to 0 miles
        self.assertEqual(km_to_miles(0), 0)

if __name__ == '__main__':
    unittest.main()
