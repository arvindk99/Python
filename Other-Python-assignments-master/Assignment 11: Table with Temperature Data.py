"""Assignment Seven:Filter List

Author: Arvind Kumar
CWID: 20372024
Date: 11/7/2018

"""
import math

default_unit = 0

units = {
0: ("Celsius", "C"),
1: ("Fahrenheit", "F"),
2: ("Kelvin", "K"),
5: ("Rankine", "R")
}

days     = {
    0 : "SUN",
    1 : "MON",
    2 : "TUE",
    3 : "WED",
    4 : "THU",
    5 : "FRI",
    6 : "SAT"
}

hours = {
    0 : "Mid-1AM  ",
    1 : "1AM-2AM  ",
    2 : "2AM-3AM  ",
    3 : "3AM-4AM  ",
    4 : "4AM-5AM  ",
    5 : "5AM-6AM  ",
    6 : "6AM-7AM  ",
    7 : "7AM-8AM  ",
    8 : "8AM-9AM  ",
    9 : "9AM-10AM ",
    10 : "10AM-11AM",
    11 : "11AM-NOON",
    12 : "NOON-1PM ",
    13 : "1PM-2PM  ",
    14 : "2PM-3PM  ",
    15 : "3PM-4PM  ",
    16 : "4PM-5PM  ",
    17 : "5PM-6PM  ",
    18 : "6PM-7PM  ",
    19 : "7PM-8PM  ",
    20 : "8PM-9PM  ",
    21 : "9PM-10PM ",
    22 : "10PM-11PM",
    23 : "11PM-MID ",
}

def convert_units(celsius_value, units):
    if units == 0:
#        print("The temperature is: ", celsius_value)
        return celsius_value
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

    print("Main Menu\n"
          "---------\n"
          "1 - Process a new data file\n"
          "2 - Choose units\n"
          "3 - Edit room filter\n"
          "4 - Show summary statistics\n"
          "5 - Show temperature by date and time\n"  #
          "6 - Show histogram of temperatures\n"
          "7 - Quit\n")
    print(current_set.get_avg_temperature_day_time(filter_list, 5, 7))

    try:
        massive_input = int(input("What is your choice? "))

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
            if len(valid_sensor_number) != 0:
#                print_filter(sensor_list, valid_sensor_number)
                change_filter(sensors, sensor_list, valid_sensor_number)
            else:
#                print_filter(sensor_list, filter_list)
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
    abc = False
    file_name = input("Please enter a Filename of the Data Set: ")
    check = current_set.process_file(file_name)
    if check == True:
        print("Loaded", current_set.get_loaded_temps(), "samples.")
    elif check == False:
        print("Please Enter a valid Filename.")
        inputs()
    while abc == False:
        another = (input("Enter a name for this Data Set between 3 and 20 \
characters."))
        hello = current_set.set_name(another)
        if hello == True:
            break
        elif hello == False:
            abc = False

def choose_units():
    unit_flag=False
    global default_unit
    while unit_flag == False:
        default_value = units.get(default_unit)
        print('Current units in ', default_value[0])
        unit_input = input("Choose new units\n"
                           "0 - Celcius\n"
                           "1 - Fahrenheit\n"
                           "2 - Kelvin\n"
                           " \n"
                           "Which unit? ")
        if unit_input.isdigit() == True:
            if (int(unit_input) == 0):
                unit_flag = True
                default_unit = int(0)
                inputs()
            elif (int(unit_input) ==1):
                unit_flag = True
                default_unit = int(1)
                inputs()
            elif (int(unit_input) ==2):
                unit_flag = True
                default_unit = int(2)
                inputs()

            else:
                unit_flag = False
                default_unit = default_unit
                print('Please choose a unit from the list')
        else:
            print('*** Please enter a number only ***')
            default_unit = default_unit
            unit_flag = False

def change_filter(sensors, sensor_list, active_sensors):
    sensor_list = recursive_sort(sensor_list)
    while True:
        print()
        print_filter(sensor_list, active_sensors)
        print()
        choice = input("Type the sensor number to toggle (e.g.4201) or x \
to end ")
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
    if current_set.data_set == None:
        return None
    else:
        if current_set.data_set == []:
            print('Please load data file and make sure at least one sensor \
is active')
        else:
            temp_tuple = current_set.get_summary_statistics(sensor_list)
            if default_unit == int(0):
                temp_unit = 'C'
                min_temperature = convert_units(temp_tuple[0], 0)
                max_temperature = convert_units(temp_tuple[1], 0)
                average_temp = convert_units(temp_tuple[2], 0)
            elif default_unit == int(1):
                temp_unit = 'F'
                min_temperature = convert_units(temp_tuple[0], 1)
                max_temperature = convert_units(temp_tuple[1], 1)
                average_temp = convert_units (temp_tuple[2], 1)
            elif default_unit == int(2):
                temp_unit = 'K'
                min_temperature = convert_units(temp_tuple[0], 2)
                max_temperature = convert_units(temp_tuple[1], 2)
                average_temp = convert_units(temp_tuple[2], 2)

            print('Minimum Temperature: ', str(round(min_temperature,2)),\
temp_unit)
            print('Maximum Temperature: ', str(round(max_temperature,2)),\
temp_unit)
            print('Average Temperature: ', str(round(average_temp,2)), \
temp_unit)
            print("\n")

def print_temp_by_day_time():
    default_value = units.get(default_unit)
    print('Units are in ', default_value[0])

    for day in days:
        print("\t  ",days.get(day), end=" ")
    print()

    for i in hours:
        print(hours.get(i), end=" ")
        for j in days:
            temp = current_set.get_avg_temperature_day_time(filter_list,j,i)
            if temp == None:
                print( "---", end="     ")
            else:
                temp = convert_units(temp, default_unit)
                if default_unit == 2:
                    print (round(temp,1), end= "   ")
                else:
                    print(round(temp,1), end="    ")
        print()

def print_histogram():
    print(filter_list)


def programquit():
    print("Thank you for using the STEM Center Temperature Project")
    quit()

sensors = {'4213': ('STEM Center', 0),
           '4201': ('Foundations Lab', 1),
           '4204': ('CS Lab', 2),
           '4218': ('Workshop Room', 3),
           '4205': ('Tiled Room', 4),
           'Out': ('Outside', 5)}

sensor_list = [(key, value[0], value[1]) for key, value in sensors.items()]

filter_list = [i for i in range(0, 6)]


class TempDataset:
    num_objects = 0
    def __init__(self):
        self.data_set = []
        self.name_dataset = "Unnamed"
        self.name = "(undefined)"
        self.filename= "(undefined)"
        TempDataset.num_objects = TempDataset.num_objects + 1

    def get_num_objects():
        return TempDataset.num_objects

    def get_name(self):
        return self.name

    def set_name(self, name):
        if len(name) >= 3 and len(name) <= 20:
            self.name = name
            return True
        else:
            return False


    def process_file(self, filename):
        try:
            my_file = open(filename, 'r')
            for next_line in my_file:
                my_tuple = tuple(next_line.rstrip('\n').split(","))
                if (my_tuple[4] in (None, "") or my_tuple[3] != 'TEMP' or \
my_tuple[1] == 'Data request'):
                    continue
                else:
                    self.data_set.append(my_tuple)
            self.data_set = [[int(x[0]),math.floor((float(x[1])*24)),\
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
        temperature = []
        if self.data_set == None:
            return None
        else:
            if self.data_set == []:
                print('Please load data file and make sure at least one \
sensor  is active')
            else:
                for i in active_sensors:
                    for j in self.data_set:
                        if (i[2] == j[2]):
                            temperature.append(j[3])

                min_temperature = min(temperature)
                max_temperature = max(temperature)
                avg_temperature = round(sum(temperature)/len(temperature), 2)

            return (min_temperature, max_temperature, avg_temperature)

    def get_avg_temperature_day_time(self, active_sensors, day, time):
        count = 0
        sum = 0
        average = 0
        if self.data_set == None or self.data_set ==[]:
            return None
        else:
            for i in self.data_set:
                if i[2] in active_sensors and i[0] == day and i[1] == time:
                    count = count +1
                    sum = sum + (i[3])
                    average = sum/count
                else:
                    continue
        if count != 0:
            return(average)
        else:
            return None

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
"""