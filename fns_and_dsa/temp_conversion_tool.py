# Global variables for conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
        # Input temperature and unit
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Validate unit input
        if unit not in ['C', 'F']:
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

        # Convert based on unit
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {converted_temp:.1f}°F")
        else:  # unit == 'F'
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {converted_temp:.1f}°C")

    except ValueError as e:
        print(f"Error: {e}. Please enter a numeric value for temperature and 'C' or 'F' for unit.")

if __name__ == "__main__":
    main()