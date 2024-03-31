from event import Event
from artwork import Artwork


class Exhibition(Event):
    """class representing exhibition"""
    def __init__(self, event_type, location, start_date, end_date, artworks=None):
            super().__init__(event_type, start_date=start_date,end_date=end_date)  # inheriting from event
            self.location = location
            self.artworks = artworks if artworks else []  # Initialize artworks as an empty list if not provided

    def add_artwork(self, artwork): # adds an Artwork object to the artworks list if it’s an instance of the Artwork class.
        if isinstance(artwork, Artwork):
            self.artworks.append(artwork)
        else:
            raise ValueError("Invalid artwork. Please provide an Artwork object.")


    def remove_artwork(self, artwork): #removes an Artwork object from the artworks list if it exists
        if artwork in self.artworks:
            self.artworks.remove(artwork)

    def get_artworks(self): #getter method ofr artwork
        return self.artworks

    #sets the artworks list to a new list of Artwork objects
    def set_artworks(self, artworks): #  ensuring that all elements in the list are instances of the Artwork class.
        if all(isinstance(art, Artwork) for art in artworks):
            self.artworks = artworks






