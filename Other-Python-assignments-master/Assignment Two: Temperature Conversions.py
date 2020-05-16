"""Assignment One: Opening Lines

Author: Arvind Kumar
CWID: 20372024
Date: 09/30/2018

Enhancements in this release: Using user inputs and functions as a way of creating a converter.

STEM Center Temperature Project
Arvind Kumar


"""

print("STEM Center Temperature Project")
print("Arvind Kumar")
def convert_units (celsius_value, units):
    if units == 0:
        print("The temperature is: ", celsius_value)
    if units == 1:
        Fahrenheit_units = ((1.8 * celsius_value) + 32)
        return Fahrenheit_units
    if units == 2:
        Kelvin_units = 273.15 + celsius_value
        return Kelvin_units



if __name__ == "__main__":
    celsius_value = float(input("Please Enter a temperature in degrees Celsius: "))
    print("That temperature in Kelvin is ", convert_units(celsius_value, 2), " \nand ", convert_units(celsius_value, 1), " in Fahrenheit")


"""
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/arvindkumar/Desktop/UCI/second year/fall quarter/cs 3a Foothill/Assignment Two: Temperature Conversions.py"
STEM Center Temperature Project
Arvind Kumar
Please Enter a temperature in degrees Celsius: 45
That temperature in Kelvin is  318.15  
and  113.0  in Fahrenheit

Process finished with exit code 0
"""