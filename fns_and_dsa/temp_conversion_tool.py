<<<<<<< HEAD
# Global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9


# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Main program execution
=======
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return
    c_or_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if c_or_f == 'C':
        final_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {final_temp}°F")
    elif c_or_f == 'F':
        final_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {final_temp}°C")
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
>>>>>>> 85ee9aa (added the temp_conversion_tool.py file)
if __name__ == "__main__":
    temperature = input("Enter the temperature to convert: ").strip()
    conversion_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    conversion_options = ["F", "C"]

    if temperature.isdigit():
        temp = float(temperature)

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
