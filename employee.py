from abc import ABC, abstractmethod

# Abstract base class for all person-like entities
class BasePerson(ABC):
    @abstractmethod
    def get_details(self):
        # Enforces subclasses to implement this method
        pass

# Employee class inherits from BasePerson
class Employee(BasePerson):
    def __init__(self, name, age, position="Employee"):
        # Private attributes (encapsulation)
        self.__name = name
        self.__age = age
        self.__position = position
        self.address = None  # Will hold an Address object later (composition)

    # Getter for name
    @property
    def name(self):
        return self.__name

    # Getter for age
    @property
    def age(self):
        return self.__age

    # Getter for position
    @property
    def position(self):
        return self.__position

    # Alternative constructor using a class method
    @classmethod
    def from_string(cls, emp_str):
        # Example input: "Bob-25-Developer"
        name, age, position = emp_str.split("-")
        return cls(name, int(age), position)

    # Static method: utility function to check if age is within valid range
    @staticmethod
    def is_valid_age(age):
        return 18 <= age <= 65

    # Concrete implementation of the abstract method
    def get_details(self):
        return f"{self.name}, {self.age}, {self.position}"

    # Assigns an address to the employee using the nested Address class
    def set_address(self, street, city):
        self.address = self.Address(street, city)

    # String representation for easy printing
    def __str__(self):
        return self.get_details()

    # Formal representation for debugging
    def __repr__(self):
        return f"Employee('{self.name}', {self.age}, '{self.position}')"

    # Nested class to model employee address (Composition)
    class Address:
        def __init__(self, street, city):
            self.street = street
            self.city = city

        def __str__(self):
            return f"{self.street}, {self.city}"

# Manager class inherits from Employee
class Manager(Employee):
    def __init__(self, name, age, employees=None):
        # Always set position to "Manager" regardless of argument
        super().__init__(name, age, "Manager")
        # Aggregation: manager references existing employee objects
        self.employees = employees if employees else []

    # Override of get_details() for polymorphism
    def get_details(self):
        return f"{super().get_details()} - manages {len(self.employees)} employee(s)"
