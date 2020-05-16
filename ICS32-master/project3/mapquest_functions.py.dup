import mapquest_api



class elevation:
    """Creates an object which gives out the
    elevations of the locations input"""
    def __init__(self,json_output:dict):
        self._all = latandlong(json_output).latlong()
        self._info = mapquest_api.convert_elevation(self._all)
    def output(self):
        """Prints elevation"""
        dictionaries = self._info
        print()
        print("ELEVATION")
        for json_output in dictionaries:
                print(round(json_output['elevationProfile'][0]['height']))


class total_distance:
    """Creates an object which gives out the total
    distance of the locations input"""
    def __init__(self,json_output:dict):
        self._info = json_output
    def output(self):
        """Prints total distance"""
        json_output = self._info
        print("TOTAL DISTANCE:", round(json_output["route"]["distance"]),"miles")


class narrative_directions:
    """Creates an object which gives out the directions from
    location to location."""
    def __init__(self,json_output:dict):
        self._info = json_output
    def output(self):
        """Prints directions"""
        json_output = self._info
        print("\nDIRECTIONS")
        for obj in json_output["route"]["legs"]:
            for item in (obj["maneuvers"]):
                print(item['narrative'])
        print()

        
class total_time:
    """Creates an object which gives out the total time
    from location to location"""
    def __init__(self,json_output:dict):
        self._info = json_output
    def output(self):
        """Prints total time"""
        json_output = self._info
        data = json_output["route"]["time"] / 60
        print("TOTAL TIME:", round(data), 'minutes')
        print()

class latandlong:
    """Creates an object which gives out the latitude and longitude
    from location to location"""
    def __init__(self,json_output:dict):
        self._info = json_output
    def output(self):
        """Prints latitude and longitude"""
        json_output = self._info
        data = json_output["route"]["locations"]
        print("\nLATLONGS")
        for obj in data:
            lat = (obj["displayLatLng"]["lat"])
            lng = ((obj["displayLatLng"]["lng"]))
            if lat > 0:
                direction_lat = "N"
            else:
                direction_lat = "S"
            if lng > 0:
                direction_lng = "E"
            else:
                direction_lng = "W"
            print('{0:.2f}'.format(abs(lat))+direction_lat + " " + '{0:.2f}'.format(abs(lng)) + direction_lng)           
    def latlong (self) -> list:
        """Gets elevation url parameters."""
        json_output = self._info
        data = json_output["route"]["locations"]
        lat_long_list = []
        for obj in data:
            lat_long = []
            lat_long.append(obj["displayLatLng"]["lat"])
            lat_long.append((obj["displayLatLng"]["lng"]))
            lat_long_list.append(lat_long)
        return lat_long_list

class Sorter:
    """Prints in order of input requested"""
    def __init__(self,json_output:dict,input_list:list):
        self._info = json_output
        self._input = input_list
    def sorted_output(self):
        info = self._info
        input_list = self._input
        sorted_list = []
        if info['info']['messages'] == []:
            for obj in input_list:
                if obj == "LATLONG":
                    sorted_list.append(latandlong(info))
                elif obj == "STEPS":
                    sorted_list.append(narrative_directions(info))
                elif obj == "TOTALTIME":
                    sorted_list.append(total_time(info))
                elif obj == "TOTALDISTANCE":
                    sorted_list.append(total_distance(info))
                elif obj == "ELEVATION":
                    sorted_list.append(elevation(info))
                else:
                  pass
            return sorted_list
        else:
            return None
    def returnOutput(self):
        """Returns output as per the requested order."""
        output = self.sorted_output()
        if output == None:
            print('\nNO ROUTE FOUND')
        else:
            try:
                for obj in output:
                    obj.output()
            finally:
                print()
                print("Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")
                
                
                

