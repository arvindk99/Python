"""Assignment Seven:Filter List

Author: Arvind Kumar
CWID: 20372024
Date: 11/7/2018

Enhancements in this release: Using methods of filtering.

[('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 5)]
[('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4213', 'STEM Center', 0), ('4205', 'Tiled Room', 4), ('4218', 'Workshop Room', 3), ('Out', 'Outside', 5)]


"""



def convert_units(celsius_value, units):
    if units == 0:
        print("The temperature is: ", celsius_value)
    if units == 1:
        Fahrenheit_units = ((1.8 * celsius_value) + 32)
        return Fahrenheit_units
    if units == 2:
        Kelvin_units = 273.15 + celsius_value
        return Kelvin_units

def recursive_sort(list_to_sort, key=0):
    '''Since my Assignment 6 and the recursive sort function did not meet
    the requirements properly, I will be using the professor's solution to
    guide this code.'''
    length = len(list_to_sort)
    if length <= 1:
        return list_to_sort
    swaplist = list_to_sort.copy()
    for i in range(0, length - 1):
        if swaplist[i][key] > swaplist[i + 1][key]:
            (swaplist[i], swaplist[i + 1]) = \
                (swaplist[i + 1], swaplist[i])
    return recursive_sort(swaplist[0:length-1], key)+ swaplist[length-1:length]



def inputs():
    try:
        massive_input = int(input("Main Menu\n"
                                  "---------\n"
                                  "1 - Process a new data file\n"
                                  "2 - Choose units\n"
                                  "3 - Edit room filter\n"
                                  "4 - Show summary statistics\n"
                                  "5 - Show temperature by date and time\n"  #
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
            print_filter(sensor_list, filter_list)
            change_filter(sensors, sensor_list, filter_list)
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

def print_filter(sensor_list, filter_list):
    for sensor in sensor_list:
        print(sensor[0], sensor[1], sep=': ', end='')
        print(' [ACTIVE]') if sensor[2] in filter_list else print('')

def new_file():
    pass

def choose_units():
    pass


def change_filter(sensors, sensor_list, active_sensors):
    while True:
        print()
        print_filter(sensor_list, active_sensors)
        print()
        print("Type the sensor number to toggle (e.g.", sensor_list[0][0],
              ") or x to end", sep='', end=' ')
        choice = input()
        if choice == "x":
            break
        if choice in sensors:
            if sensors[choice][1] in filter_list:
                filter_list.remove(sensors[choice][1])
            else:
                filter_list.append(sensors[choice][1])
        else:
            print("Invalid Sensor")


def print_summary_statistics():
    pass


def print_temp_by_day_time():
    pass


def print_histogram():
    pass


def programquit():
    print("Thank you for using the STEM Center Temperature Project")
    quit()


sensors = {'4213': ('STEM Center', 0), '4201': ('Foundations Lab', 1),
           '4204': ('CS Lab', 2), '4218': ('Workshop Room', 3),
           '4205': ('Tiled Room', 4), 'Out': ('Outside', 5)}

sensor_list = [(key, value[0], value[1]) for key, value in sensors.items()]

filter_list = [v[1] for k, v in sensors.items()]

sensor_list = recursive_sort(sensor_list, 0)


if __name__ == "__main__":
    print("STEM Center Temperature Project")
    print("Arvind Kumar\n")
    inputs()
    while inputs() == False:
        if inputs() == True:
            break


            # celsius_value = float(input("Please Enter a temperature in degrees Celsius: "))
            # print("That temperature in Kelvin is ", convert_units(celsius_value, 2), " \nand ", convert_units(celsius_value, 1), " in Fahrenheit")

"""/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/arvindkumar/Desktop/UCI/second year/fall quarter/cs 3a Foothill/assignment 7: Filter List.py"
STEM Center Temperature Project
Arvind Kumar

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
 
What is your choice? 3


4201 : Foundations Lab [ACTIVE]
4204 : CS Lab [ACTIVE]
4205 : Tiled Room [ACTIVE]
4213 : STEM Center [ACTIVE]
4218 : Workshop Room [ACTIVE]
Out : Outside [ACTIVE]

 Type the sensor number to toggle (e.g.4201) or x to end 4201


4201 : Foundations Lab
4204 : CS Lab [ACTIVE]
4205 : Tiled Room [ACTIVE]
4213 : STEM Center [ACTIVE]
4218 : Workshop Room [ACTIVE]
Out : Outside [ACTIVE]

 Type the sensor number to toggle (e.g.4201) or x to end 4205


4201 : Foundations Lab
4204 : CS Lab [ACTIVE]
4205 : Tiled Room
4213 : STEM Center [ACTIVE]
4218 : Workshop Room [ACTIVE]
Out : Outside [ACTIVE]

 Type the sensor number to toggle (e.g.4201) or x to end 4205


4201 : Foundations Lab
4204 : CS Lab [ACTIVE]
4205 : Tiled Room [ACTIVE]
4213 : STEM Center [ACTIVE]
4218 : Workshop Room [ACTIVE]
Out : Outside [ACTIVE]

 Type the sensor number to toggle (e.g.4201) or x to end 400
Invalid Sensor


4201 : Foundations Lab
4204 : CS Lab [ACTIVE]
4205 : Tiled Room [ACTIVE]
4213 : STEM Center [ACTIVE]
4218 : Workshop Room [ACTIVE]
Out : Outside [ACTIVE]

 Type the sensor number to toggle (e.g.4201) or x to end x
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