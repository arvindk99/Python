"""Assignment One: Opening Lines

Author: Arvind Kumar
CWID: 20372024
Date: 10/07/2018

Enhancements in this release: Using and manipulating loops.

STEM Center Temperature Project
Arvind Kumar


"""

print("STEM Center Temperature Project")
print("Arvind Kumar\n")
 def convert_units (celsius_value, units):
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
                              "5 - Show temperature by date and time\n"
                              "6 - Show histogram of temperatures\n"
                              "7 - Quit\n"
                              " \n"
                              "What is your choice? "))
    except ValueError:
        print("\n*** Please enter an integer only ***\n")
        return False
    if massive_input < 8 and massive_input>0:
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
    print("Function 1 will run")

def choose_units():
    print("Function 2 will run")

def change_filter():
    print("Function 3 will run")

def print_summary_statistics():
    print("Function 4 will run")

def print_temp_by_day_time():
    print("Function 5 will run")

def print_histogram():
    print("Function 6 will run")

def programquit():
    print("Thank you for using the STEM Center Temperature Project")
    quit()


if __name__ == "__main__":
    inputs()
    while inputs() == False:
        if inputs() == True:
            break


    #celsius_value = float(input("Please Enter a temperature in degrees Celsius: "))
    #print("That temperature in Kelvin is ", convert_units(celsius_value, 2), " \nand ", convert_units(celsius_value, 1), " in Fahrenheit")


"""
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/arvindkumar/Desktop/UCI/second year/fall quarter/cs 3a Foothill/Assignment Three: Menu Functionality.py"
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
Function 1 will run
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
 
What is your choice? 2
Function 2 will run
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
Function 3 will run
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
 
What is your choice? 4
Function 4 will run
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
 
What is your choice? 5
Function 5 will run
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
 
What is your choice? 6
Function 6 will run
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
 
What is your choice? t

*** Please enter an integer only ***

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
 
What is your choice? 12

Enter a number between 1 and 7.

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
 
What is your choice? -1

Enter a number between 1 and 7.

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