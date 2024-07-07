# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Main program execution
if __name__ == "__main__":
    # User input for temperature and type of conversion
    temperature = input("Enter the temperature to convert: ").strip()
    conversion_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Valid conversion options
    conversion_options = ["F", "C"]

    # Input validation
    if temperature.isdigit():  # Check if input is a digit
        temp = float(temperature)  # Convert input to float

        if conversion_type in conversion_options:
            if conversion_type == "F":
                converted_temp = convert_to_celsius(temp)
                print(f"{temp}°F is {converted_temp}°C")
            elif conversion_type == "C":
                converted_temp = convert_to_fahrenheit(temp)
                print(f"{temp}°C is {converted_temp}°F")
        else:
            print("Incorrect conversion option. Please enter 'C' or 'F'.")
    else:
        print("Invalid temperature input. Please enter a numeric value.")
