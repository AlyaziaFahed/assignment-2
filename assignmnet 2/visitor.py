from person import Person
from enum import Enum

# Enumeration representing different types of visitors.
class VisitorType(Enum):
    ADULT = (1, "Adult")
    CHILD = (2, "Child")
    SENIOR = (3, "Senior")
    TEACHER_STUDENT = (4, "Teacher or Student")
    GROUP = (5, "Group")

# Visitor class that inherits from the Person class and adds visitor-specific attributes and methods.
class Visitor(Person):
    """class representing Visitor"""
    def __init__(self, name, age, national_id, email_id, type_of_visitor):
        # Initialize the superclass (Person) with the common attributes.
        super().__init__(name, age, national_id, email_id)
        # Set the type of visitor using the VisitorType enum
        # Using a single underscore to indicate a protected attribute.
        self._type_of_visitor = VisitorType(type_of_visitor)
        # Initialize the visitor's ticket as None, indicating no ticket has been assigned yet.
        # Using a single underscore to indicate a protected attribute.
        self._ticket = None

    # Getter method to return the type of visitor.
    def get_type_of_visitor(self):
        # Accessing the protected type of visitor attribute.
        return self._type_of_visitor

    # Setter method to update the type of visitor.
    # This method converts the input to uppercase to match the VisitorType enum
    def set_type_of_visitor(self, type_of_visitor):
        self._type_of_visitor = VisitorType(type_of_visitor.upper())

    # Getter method to return the visitor's ticket.
    def get_ticket(self):
        return self._ticket

    # Setter method to update the visitor's ticket.
    def set_ticket(self, ticket):
        self._ticket = ticket

    # Method to assign a ticket to the visitor.
    def assign_ticket(self, ticket):
        # Import Ticket class locally to avoid circular import issues.
        from ticket import Ticket
        # Check if the input is an instance of Ticket before assignment.
        if isinstance(ticket, Ticket):
            # Assigning the ticket to the protected ticket attribute.
            self._ticket = ticket

    # Method to purchase a ticket for an event.
    def purchase_ticket(self, event, location, duration, purchase_method):
        # Create a new Ticket object with the provided details.
        ticket = Ticket(self._type_of_visitor, event, location, duration)
        # Assign the newly purchased ticket to the visitor.
        self.assign_ticket(ticket)
        # Retrieve and return the ticket details, including the purchase method.
        ticket_details = ticket.display_ticket_details()
        return f"{ticket_details}"