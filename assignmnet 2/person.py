class Person:
    """Class representing a person"""

    def __init__(self, name, age, national_id, email_id):
        # Initialize the Person object with name, age, national ID, and email ID.
        # Using a single underscore to indicate a protected attribute.
        self._name = name
        self._age = age
        self._national_id = national_id
        self._email_id = email_id

    # Getter method to return the person's name.
    def get_name(self):
        return self._name

    # Getter method to return the person's age.
    def get_age(self):
        return self._age

    # Getter method to return the person's national ID.
    def get_national_id(self):
        return self._national_id

    # Getter method to return the person's email ID.
    def get_email_id(self):
        return self.email_id  # Should be self._email_id

    # Setter method to update the person's name.
    def set_name(self, name):
        self._name = name

    # Setter method to update the person's age.
    # This method also includes validation to ensure the age is not negative.
    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Age cannot be negative")  # Error message for invalid age input.

    # Setter method to update the person's national ID.
    def set_national_id(self, national_id):
        self._national_id = national_id

    # Setter method to update the person's email ID.
    def set_email_id(self, email_id):
        self.email_id = email_id
