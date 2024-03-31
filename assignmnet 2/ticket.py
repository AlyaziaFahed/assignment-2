from visitor import VisitorType

class Ticket:
    """class representing ticket"""
    # Constructor of the Ticket class.
    def __init__(self, type_of_visitor, event, location, duration):
        # These attributes are private.
        self.__type_of_visitor = type_of_visitor  # Access enum member directly
        self.__event = event
        self.__location = location
        self.__duration = duration
        # Calculate price after setting type_of_visitor
        self.__price = self.calculate_price()

    # Getter method for the price attribute.
    def get_price(self):
        return self.__price

    # Setter method for the private price attribute.
    def set_price(self, price):
        self.__price = price

    # Method to calculate the price of the ticket based on visitor type.
    def calculate_price(self):
        base_price = 63  # Base price for adults
        vat_rate = 0.05  # 5% VAT

        # Check visitor type and apply pricing rules.
        if self.__type_of_visitor in [VisitorType.CHILD, VisitorType.SENIOR, VisitorType.TEACHER_STUDENT]:
            return 0  # Free ticket for these categories.
        elif self.__type_of_visitor == VisitorType.GROUP:
            # Apply 50% discount for groups.
            return (base_price / 2) * (1 + vat_rate)
        elif self.__type_of_visitor == VisitorType.ADULT:
            # Apply VAT for adults.
            return base_price * (1 + vat_rate)
        else:
            raise ValueError(f"Invalid visitor type: {self.__type_of_visitor}")

    # Getter method for the type_of_visitor attribute.
    def get_type_of_visitor(self):
        return self.__type_of_visitor

    # Setter method for the type_of_visitor attribute.
    def set_type_of_visitor(self, type_of_visitor):
        self.__type_of_visitor = VisitorType(type_of_visitor)

    # Getter method for the  event attribute.
    def get_event(self):
        return self.__event

    # Setter method for the  event attribute.
    def set_event(self, event):
        self.__event = event

    # Getter method for the location attribute.
    def get_location(self):
        return self.__location

    # Setter method for the location attribute.
    def set_location(self, location):
        self.__location = location

    # Getter method for the duration attribute.
    def get_duration(self):
        return self.__duration

    # Setter method for the  duration attribute.
    def set_duration(self, duration):
        self.__duration = duration
