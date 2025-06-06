# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius}°C")

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {fahrenheit}°F")

# User interaction
temperature_input = input("Enter the temperature to convert: ")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

# Check for valid numeric input without using try/except
if (temperature_input.replace('.', '', 1).isdigit() or
    (temperature_input.startswith('-') and temperature_input[1:].replace('.', '', 1).isdigit())):

    temperature = float(temperature_input)

    if unit.upper() == "F":
        convert_to_celsius(temperature)
    elif unit.upper() == "C":
        convert_to_fahrenheit(temperature)
    else:
        print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
else:
    print("Invalid temperature. Please enter a numeric value.")
