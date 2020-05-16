import json
import urllib.parse
import urllib.request
import mapquest_functions

MAPQUEST_API = 'NffqtX4OxBYViOC5XOFMwgbejE3O9ITU'
MAPQUEST_BASEURL = 'http://open.mapquestapi.com/directions/v2/route'
API_ELEVATION= 'http://open.mapquestapi.com/elevation/v1/profile'


def get_url (destinations: list):
    """Creates the URL for the requested locations."""
    parameters = [("key", MAPQUEST_API),("from", destinations[0])]
    for obj in range(1,len(destinations)):
        parameters.append(("to",destinations[obj]))
    return MAPQUEST_BASEURL + '?' + urllib.parse.urlencode(parameters)

def get_elevation(latlong: list) -> list:
    """Creates Elevation URLs"""
    URLS = []
    parameters = []
    for location in latlong:
        parameter = ''
        lat = str(location[0])
        lng = str(location[1])
        parameter += lat+','+lng
        parameters.append(parameter)
        
    for location in latlong:
        for index in range(len(parameters)):
            lat_long = parameters[index]
            url = API_ELEVATION + '?key=' + MAPQUEST_API + '&unit=f&latLngCollection=' + lat_long
            URLS.append(url)

    URLS = list(set(URLS))
    return URLS
    

def convert (url:str)->dict:
    """Extracts info from url and converts json objects into python object"""
    try:
        serverConnection = urllib.request.urlopen(url)
        jsonVersion = serverConnection.read().decode(encoding = 'utf-8')
        return json.loads(jsonVersion)
    except:
        serverConnection = None
    finally:
        if serverConnection != None:
            serverConnection.close()

def convert_elevation(latlong:list)->list:
    """Extracts info from elevation urls and converts json objects into python objects"""
    all_info = []
    urls = get_elevation(latlong)
    for url in urls:
        info = convert(url)
        all_info.append(info)
    return all_info
        
