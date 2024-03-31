from location import Location

class Artwork:
    """class representing artwork"""
    # Constructor for creating an Artwork object with title, artist, year of creation, location, and historical significance.
    def __init__(self, title, artist, year_of_creation, location, historical_significance):
        # Ensures the location parameter is an instance of the Location class.
        if not isinstance(location, Location):
            raise ValueError("Invalid location. Please provide a Location object.")
        self.title = title  # Title of the artwork
        self.artist = artist  # Name of the artist
        self.year_of_creation = year_of_creation  # Year the artwork was created
        self.location = location  # Location object representing where the artwork is located or stored
        self.historical_significance = historical_significance  # Textual description of the artwork's historical significance

    # Returns the title of the artwork.
    def get_title(self):
        return self.title

    # Sets title for the artwork.
    def set_title(self, title):
        self.title = title

    # Returns the name of the artist.
    def get_artist(self):
        return self.artist

    # Sets artist for the artwork.
    def set_artist(self, artist):
        self.artist = artist

    # Returns the year the artwork was created.
    def get_year_of_creation(self):
        return self.year_of_creation

    # Sets year of creation for the artwork.
    def set_year_of_creation(self, year_of_creation):
        self.year_of_creation = year_of_creation

    # Returns the location object of the artwork.
    def get_location(self):
        return self.location

    # Sets  location for the artwork. The location must be a Location object.
    def set_location(self, location):
        self.location = location

    # Returns the historical significance of the artwork.
    def get_historical_significance(self):
        return self.historical_significance

    # Sets historical significance for the artwork.
    def set_historical_significance(self, historical_significance):
        self.historical_significance = historical_significance

