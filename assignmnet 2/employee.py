from person import Person #import person class since its in a different file
class Employee(Person):
    """class representing Employee"""
    def __init__(self, name, age, national_id, email_id, employee_id):
        super().__init__(name, age, national_id, email_id)
        self._employee_id = employee_id  # Unique identifier for the employee (protected as well)

    # Getter methods for the new attributes
    def get_employee_id(self):
        return self._employee_id

    # Setter methods for the new attributes
    def set_employee_id(self, _employee_id):
        self._employee_id = _employee_id



