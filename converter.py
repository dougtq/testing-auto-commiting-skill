# Conversion Constants
CELSIUS_TO_FAHRENHEIT_RATIO = 9 / 5
FAHRENHEIT_OFFSET = 32
KM_TO_MILES_FACTOR = 0.621371

def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.
    Formula: (Celsius * 9/5) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_RATIO) + FAHRENHEIT_OFFSET

def km_to_miles(km):
    """
    Converts Kilometers to Miles.
    Factor: 0.621371
    """
    return km * KM_TO_MILES_FACTOR
