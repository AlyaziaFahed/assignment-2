from enum import Enum

class LocationType(Enum):
    # Enumeration for different types of location spaces with their names and capacities.
    PERMANENT_GALLERIES = ("Permanent Galleries", 90)
    EXHIBITION_HALLS = ("Exhibition Halls", 75)
    OUTDOOR_SPACES = ("Outdoor Spaces", 120)

class Location:
    """class representing location"""
    # Constructor of the Location class that initializes a Location object with a given type.
    def __init__(self, location_type):
        # Set the name and capacity based on the location_type value.
        # These attributes are  private
        self.__name, self.__capacity = location_type.value

    # Getter method for the private name attribute.
    def get_name(self):
        return self.__name

    # Setter method for the private name attribute.
    def set_name(self, name):
        self.__name = name

    # Getter method for the location type.
    def get_location_type(self):
        return self.__type_of_location

    # Setter method for the location type.
    def set_location_type(self, type_of_location):
        # It assumes that type_of_location is a valid value of the LocationType Enum.
        self.__type_of_location = LocationType(type_of_location)

    # Getter method for the private capacity attribute.
    def get_capacity(self):
        return self.__capacity

    # Setter method for the private capacity attribute.
    def set_capacity(self, capacity):
        self.__capacity = capacity