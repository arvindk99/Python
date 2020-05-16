"""Assignment 9:File Import

Author: Arvind Kumar
CWID: 20372024
Date: 11/23/2018

Enhancements in this release: Using methods of filtering.

[('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 5)]
[('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4213', 'STEM Center', 0), ('4205', 'Tiled Room', 4), ('4218', 'Workshop Room', 3), ('Out', 'Outside', 5)]


"""


import math

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

        if massive_input == 2:
            choose_units()
            return False
        if massive_input == 3:
#            print(fliter_list)
            if len(valid_sensor_number) !=0:
                print_filter(sensor_list, valid_sensor_number)
                change_filter(sensors, sensor_list, valid_sensor_number)
            else:
                print_filter(sensor_list, filter_list)
                change_filter(sensors, sensor_list, filter_list)
#                filter_list=valid_sensor_number
#            print_filter(sensor_list, filter_list)
#            change_filter(sensors, sensor_list, filter_list)
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
    sensor_list = recursive_sort(sensor_list)
    print('\n')
    for x in sensor_list:
        if filter_list[0] == 0:
            print(x[0],":",x[1], "[ACTIVE]")
        else:
            if x[0] in filter_list:
                print(x[0],":",x[1], "[ACTIVE]")
            else:
                print(x[0],":",x[1])


def new_file():
    abc = False
    file_name = input("Please enter a Filename of the Data Set: ")
    check = current_set.process_file(file_name)
    if check == True:
        print("Loaded", current_set.get_loaded_temps(), "samples.")
    elif check == False:
        print("Please Enter a valid Filename.")
        inputs()
    while abc == False:
        another = (input("Please provide a 3 to 20 character name for the \
dataset: "))
        hello = current_set.set_name(another)
        if hello == True:
            break
        elif hello == False:
            abc = False

def choose_units():
    pass

def change_filter(sensors, sensor_list, filter_list):
    valid_numbers = recursive_sort(sensor_list)
    for i in valid_numbers:
        valid_sensor_number.append(i[0])

    new_sensor_list=sensor_list[:]
    new_list=[]
    new_list = valid_sensor_number[:]

    userquit = False
    while userquit == False:
        try:
            sensorinput = input("Type the sensor number to toggle (e.g.4201) \
or x to end ")

            if sensorinput == 'x':
                filter_list = valid_sensor_number
                sensor_list = valid_numbers
                inputs()
                userquit = True
                #break
            elif ((sensorinput) in valid_sensor_number):
                valid_sensor_number.remove(sensorinput)
                for i in valid_numbers:
                    if i[0] == sensorinput:
                        new_sensor_list.remove(i)
                    else:
                        new_sensor_list.append(i)
            elif ((sensorinput) not in valid_sensor_number):
                if sensorinput in new_list:
                    valid_sensor_number.append(sensorinput)
                else:
                    print('Invalid Sensor')
            filter_list = valid_sensor_number
            sensor_list = valid_numbers
            print_filter(sensor_list,filter_list)
        except ValueError:
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

filter_list = [i for i in range(0, 6)]


class TempDataset:
    num_objects = 0
    def __init__(self):
#        self.data_set = None
        self.data_set = []
        self.name_dataset = "Unnamed"
        self.name = "Unnamed"
        self.filename= "(undefined)"
        TempDataset.num_objects = TempDataset.num_objects + 1

    def get_num_objects():
        return TempDataset.num_objects

    def get_name(self):
        return self.name

    def set_name(self, name):
        if len(name) >=3 and len(name) <= 20:
            self.name = name
            return True
        else:
            return False

    def process_file(self, filename):
        try:
            if filename == "":
                print('Name cannot be empty')
            else:
                self.filename = filename
            my_file = open(filename, 'r')
            for next_line in my_file:
                my_tuple = tuple(next_line.rstrip('\n').split(","))
                if my_tuple[4] in (None, "") or my_tuple[3] != 'TEMP':
                    continue

                elif my_tuple[0].isdigit():
                    self.data_set.append(my_tuple)
            self.data_set = [[int(x[0]),math.floor((float(x[1])*24)),
                              int(x[2]),float(x[4])] for x in self.data_set]
            my_file.close()
            return True
        except FileNotFoundError:
            return False

    def get_loaded_temps(self):
        if self.data_set == None:
            return None
        else:
            return len(self.data_set)


    def get_num_temps(self, active_sensors, lower_bound, upper_bound):
        if self.data_set == None:
            return None
        else:
            return 0

    def get_summary_statistics(self, active_sensors):
        if self.data_set == None:
            return None
        else:
            return (0,0,0)

    def get_avg_temperature_day_time(self, active_sensor, day, time):
        if self.data_set == None:
            return None
        else:
            return 0

current_set = TempDataset()


if __name__ == "__main__":
    recursive_sort(sensor_list, 0)
    print("STEM Center Temperature Project")
    print("Arvind Kumar\n")
    valid_sensor_number=[]
    valid_numbers=[]
    inputs()
    while inputs() == False:
        if inputs() == True:
            break

"""
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/arvindkumar/Desktop/UCI/second year/fall quarter/cs 3a Foothill/Assignment 9: File Import.py"
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
 
What is your choice? 1
Please enter a Filename of the Data Set: hello
Please Enter a valid Filename.
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
 
What is your choice? 1
Please enter a Filename of the Data Set: Temperatures2017-08-06.csv
Loaded 11724 samples.
Please provide a 3 to 20 character name for the dataset: helllooohellohellohelloelloehlloe
Please provide a 3 to 20 character name for the dataset: hello
Please provide a 3 to 20 character name for the dataset: hello
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

