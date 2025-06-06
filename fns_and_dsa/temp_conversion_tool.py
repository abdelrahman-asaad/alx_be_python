FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    temp = int(input("Enter the temperature to convert: "))
    ask = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if ask == "F":

      fahrenheit = temp
      celsius = (fahrenheit -32) *FAHRENHEIT_TO_CELSIUS_FACTOR
      print(celsius,"°C")
    else :
       print("go to celisues func")
def convert_to_fahrenheit(celsius):
          temp = int(input("enter temp in celsius: "))
          ask = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
          if ask == "C":
            celsius = temp
          fahernheit = celsius * FAHRENHEIT_TO_CELSIUS_FACTOR +32
          print(fahernheit,"°F")

convert_to_celsius(5)   
convert_to_fahrenheit(celsius=5)

    
