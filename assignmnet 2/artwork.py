from location import Location
class Artwork:
    def __init__(self, title, artist, year_of_creation, location, historical_significance):
        if not isinstance(location, Location):
            raise ValueError("Invalid location. Please provide a Location object.")
        self.title = title
        self.artist = artist
        self.year_of_creation = year_of_creation
        self.location = location
        self.historical_significance = historical_significance

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_artist(self):
        return self.artist

    def set_artist(self, artist):
        self.artist = artist

    def get_year_of_creation(self):
        return self.year_of_creation

    def set_year_of_creation(self, year_of_creation):
        self.year_of_creation = year_of_creation

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_historical_significance(self):
        return self.historical_significance

    def set_historical_significance(self, historical_significance):
        self.historical_significance = historical_significance

