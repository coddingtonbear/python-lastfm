#!/usr/bin/env python

__author__ = "Abhinav Sarkar"
__version__ = "0.1"
__license__ = "GNU Lesser General Public License"

class Geo(object):
    """A class representing an geographic location."""
    @staticmethod
    def getEvents(api, location, distance, page):
        pass
    
    @staticmethod
    def getTopArtists(api, country):
        pass
    
    @staticmethod
    def getTopTracks(api, country):
        pass

class Venue(object):
    """A class representing a venue of an event"""
    def __init__(self,
                 name = None,
                 location = None,
                 url = None):
        self.__name = name
        self.__location = location
        self.__url = url

    def getName(self):
        return self.__name

    def getLocation(self):
        return self.__location

    def getUrl(self):
        return self.__url
    
    name = property(getName, None, None, "Name's Docstring")

    location = property(getLocation, None, None, "Location's Docstring")

    url = property(getUrl, None, None, "Url's Docstring")
    
    def __eq__(self, other):
        return sefl.url == other.url
    
class Location(object):
    """A class representing a location of an event"""
    xmlns = "http://www.w3.org/2003/01/geo/wgs84_pos#"
    
    def __init__(self,
                 api,
                 name = None,
                 city = None,
                 country = None,
                 street = None,
                 postalCode = None,
                 latitude = None,
                 longitude = None,
                 timezone = None):
        self.__api = api
        self.__name = name
        self.__city = city
        self.__country = country
        self.__street = street
        self.__postalCode = postalCode
        self.__latitude = latitude
        self.__longitude = longitude
        self.__timezone = timezone
        
    def getName(self):
        return self.__city

    def getCity(self):
        return self.__city

    def getCountry(self):
        return self.__country

    def getStreet(self):
        return self.__street

    def getPostalCode(self):
        return self.__postalCode

    def getLatitude(self):
        return self.__latitude

    def getLongitude(self):
        return self.__longitude

    def getTimezone(self):
        return self.__timezone
    
    name = property(getName, None, None, "Name's Docstring")

    city = property(getCity, None, None, "City's Docstring")

    country = property(getCountry, None, None, "Country's Docstring")

    street = property(getStreet, None, None, "Street's Docstring")

    postalCode = property(getPostalCode, None, None, "PostalCode's Docstring")

    latitude = property(getLatitude, None, None, "Latitude's Docstring")

    longitude = property(getLongitude, None, None, "Longitude's Docstring")

    timezone = property(getTimezone, None, None, "Timezone's Docstring")        
    
    def getEvents(self,
                  distance = None,
                  page = None):
        return Geo.getEvents(self.__api, self.name, distance, page)
    
    events = property(getEvents, None, None, "Event's Docstring")
    
    def __eq__(self, other):
        return self.latitude == other.latitude and self.longitude == other.longitude
    
class Country(object):
    """A class representing a country."""
    def __init__(self,
                 api,
                 name = None):
        self.__api = api
        self.__name = name

    def getName(self):
        return self.__name
    
    name = property(getName, None, None, "Name's Docstring")
    
    def getTopArtists(self):
        return Geo.getTopArtists(self.__api, self.name)
    
    topArtists = property(getTopArtists, None, None, "Docstring")
    topArtist = property(
                         lambda self: len(self.topArtists) and self.topArtists[0],
                         None, None, "Docstring"                         
                         )
    
    def getTopTracks(self):
        return Geo.getTopTracks(self.__api, self.name)
    
    topTracks = property(getTopTracks, None, None, "Docstring")
    topTrack = property(lambda self: len(self.topTracks) and self.topTracks[0],
                        None, None, "Docstring")
    
    def __eq__(self, other):
        return self.name == other.name