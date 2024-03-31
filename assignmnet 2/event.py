from ticket import Ticket
from location import Location, LocationType
from enum import Enum
from datetime import date, timedelta
import random

# Define an enumeration for different types of events.
class EventType(Enum):
    ART_EXHIBITION = "Art Exhibition"
    MUSIC_FESTIVAL = "Music Festival"
    SCIENCE_CONFERENCE = "Science Conference"
    FOOD_FAIR = "Food Fair"

# Define the Event class.
class Event:
    """class representing event """
    # Constructor of the Event class.
    def __init__(self, event_type, start_date=date(2024, 1, 1), end_date=date(2024, 12, 31)):
        # Set the name of the event based on the EventType passed.
        self.name = event_type.value
        # Assign a random location to the event.
        self.location = Location(random.choice(list(LocationType)))
        self.start_date = start_date
        # Set a random end date between the start date and the provided end date.
        self.end_date = self.random_date(self.start_date, end_date)
        # Initialize an empty list to hold tickets for the event.
        self.tickets = []

    # Static method to generate a random date within a date range.
    @staticmethod
    def random_date(start_date, end_date):
        # Calculate a random number of days to add to the start_date.
        random_days = random.randint(0, (end_date - start_date).days)
        # Return the new date after adding the random number of days.
        return start_date + timedelta(days=random_days)

    # Method to create a ticket for the event.
    def create_ticket(self, visitor_type, price=None):
        # Instantiate a new Ticket object for the visitor.
        new_ticket = Ticket(visitor_type, self.name, price)
        # Add the new ticket to the event's tickets list.
        self.tickets.append(new_ticket)
        # Return the newly created ticket.
        return new_ticket

    # Method to get the name of the event.
    def get_name(self):
        return self.name

    # Method to set the name of the event.
    def set_name(self, name):
        self.name = name

    # Method to get the name of the event's location.
    # This assumes that the Location class has a method get_name to return the location's name.
    def get_location(self):
        return self.location.get_name()

    # Method to set the event's location.
    def set_location(self, location):
        # Check if the passed object is an instance of Location.
        if isinstance(location, Location):
            self.location = location

    # Method to get the start date of the event.
    def get_start_date(self):
        return self.start_date

    # Method to set the start date of the event.
    def set_start_date(self, start_date):
        self.start_date = start_date

    # Method to get the end date of the event.
    def get_end_date(self):
        return self.end_date

    # Method to set the end date of the event.
    def set_end_date(self, end_date):
        self.end_date = end_date