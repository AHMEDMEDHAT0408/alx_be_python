# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


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


if __name__ == "__main__":
    main()
