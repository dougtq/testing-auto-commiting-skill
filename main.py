from converter import celsius_to_fahrenheit, km_to_miles

def main():
    print("Welcome to the Unit Converter!")
    print("1. Celsius to Fahrenheit")
    print("2. Kilometers to Miles")
    
    choice = input("Select an option (1-2): ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == '2':
        km = float(input("Enter distance in Kilometers: "))
        miles = km_to_miles(km)
        print(f"{km} km is equal to {miles} miles")
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    main()
