import mapquest_api
from mapquest_functions import Sorter


def trip_locations():
    """Gets inputs of number and where locations are."""
    try:
        numberinput = int(input())
        if numberinput<2:
            print("Error")
            return trip_locations()
        location_list = []
        for i in range(numberinput):
            try:
                location_list.append(input())
            except:
                print('ERROR')
        return location_list
    except (ValueError, IndexError):
        print('ERROR')
        return trip_locations()


def action_output():
    """Gets the requested commands"""
    number_input = int(input())
    if number_input > 5:
        print("ERROR")
        return action_output()
    output_list = []
    for obj in range(number_input):
        output_list.append(input())
    return output_list



if __name__ == "__main__":
    try:
        step_1 = trip_locations()
        step_2 = action_output()
        printer = Sorter(mapquest_api.convert(mapquest_api.get_url(step_1)),step_2)
        printer.returnOutput()
    except:
        print('MAPQUEST ERROR')
