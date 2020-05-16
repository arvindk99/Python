"""Assignment Six: Sorting

Author: Arvind Kumar
CWID: 20372024
Date: 10/14/2018

Enhancements in this release: Using and manipulating loops.

STEM Center Temperature Project
Arvind Kumar


"""


print("STEM Center Temperature Project")
print("Arvind Kumar\n")


def convert_units(celsius_value, units):
    if units == 0:
        print("The temperature is: ", celsius_value)
    if units == 1:
        Fahrenheit_units = ((1.8 * celsius_value) + 32)
        return Fahrenheit_units
    if units == 2:
        Kelvin_units = 273.15 + celsius_value
        return Kelvin_units


def inputs():
    try:
        massive_input = int(input("Main Menu\n"
                                  "---------\n"
                                  "1 - Process a new data file\n"
                                  "2 - Choose units\n"
                                  "3 - Edit room filter\n"
                                  "4 - Show summary statistics\n"
                                  "5 - Show temperature by date and time\n"   #
                                  "6 - Show histogram of temperatures\n"
                                  "7 - Quit\n"
                                  " \n"
                                  "What is your choice? "))
    except ValueError:
        print("\n*** Please enter an integer only ***\n")
        return False
    if massive_input < 8 and massive_input > 0:
        if massive_input == 1:
            new_file()
            return False
        if massive_input == 2:
            choose_units()
            return False
        if massive_input == 3:
            change_filter()
            return False
        if massive_input == 4:
            print_summary_statistics()
            return False
        if massive_input == 5:
            print_temp_by_day_time()
            return False
        if massive_input == 6:
            print_histogram()
            return False
        if massive_input == 7:
            programquit()
            return True
    else:
        print("\nEnter a number between 1 and 7.\n")
        return False


def new_file():
    pass


def choose_units():
    pass


def change_filter():
    pass


def print_summary_statistics():
    pass


def print_temp_by_day_time():
    pass


def print_histogram():
    pass

def programquit():
    print("Thank you for using the STEM Center Temperature Project")
    quit()

sensors = {'4213':('STEM Center', 0), '4201':('Foundations Lab', 1),
           '4204':('CS Lab', 2), '4218':('Workshop Room', 3),
           '4205':('Tiled Room', 4), 'Out':('Outside', 5)}

sensor_list = [(key,value[0], value[1]) for key,value in sensors.items()]

print(sensor_list)

filter_list = [i for i in range(0,6)]

print("Testing sensors:")
if sensors["4213"][0] == "STEM Center" and sensors["Out"][1] == 5:
    print("Pass")
else:
    print("Fail")

print("Testing sensor_list length:")
if len(sensor_list) == 6:
    print("Pass")
    print("Testing sensor_list content:")
    for item in sensor_list:
        if item[1] != sensors[item[0]][0]:
            print("Fail")
            break
    else:
        print("Pass")

print("Testing filter_list length:")
if len(filter_list) == 6:
    print("Pass")
else:
    print("Fail")

print("Testing filter_list content:")
if sum(filter_list) == 15:
    print("Pass")
else:
    print("Fail")


if __name__ == "__main__":
    inputs()
    while inputs() == False:
        if inputs() == True:
            break


            # celsius_value = float(input("Please Enter a temperature in degrees Celsius: "))
            # print("That temperature in Kelvin is ", convert_units(celsius_value, 2), " \nand ", convert_units(celsius_value, 1), " in Fahrenheit")

"""
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/arvindkumar/Desktop/UCI/second year/fall quarter/cs 3a Foothill/Assignment four: Creating a Sensor Dictionary and List.py"
STEM Center Temperature Project
Arvind Kumar

[('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 5)]
Testing sensors:
Pass
Testing sensor_list length:
Pass
Testing sensor_list content:
Pass
Testing filter_list length:
Pass
Testing filter_list content:
Pass
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
 
What is your choice? 7
Thank you for using the STEM Center Temperature Project

Process finished with exit code 0
"""