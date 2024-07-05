FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    temp = float(input("Enter the temperature to convert: "))
    c_or_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    final_temp = 0
    if c_or_f == 'C':
        final_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {final_temp}°F")
    else:
        final_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {final_temp}°C")

if __name__ == "__main__":
    main()
