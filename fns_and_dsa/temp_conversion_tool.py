# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
temp_input = input("Enter the temperature to convert: ")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

# Basic numeric input validation (simulate ValueError)
if (
    temp_input.replace(".", "", 1).isdigit()
    or (temp_input.startswith("-") and temp_input[1:].replace(".", "", 1).isdigit())
):
    temperature = float(temp_input)

    if unit == "F":
        result = convert_to_celsius(temperature)
        print(str(temperature) + "°F is " + str(result) + "°C")
    elif unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(str(temperature) + "°C is " + str(result) + "°F")
    else:
        print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
else:
    print("Invalid temperature. Please enter a numeric value.")
