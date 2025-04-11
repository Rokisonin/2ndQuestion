from abc import ABC, abstractmethod

class BasePerson(ABC):
    @abstractmethod
    def get_details(self):
        pass

class Employee(BasePerson):
    def __init__(self, name, age, position="Employee"):
        self.__name = name
        self.__age = age
        self.__position = position
        self.address = None

    # Encapsulation
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def position(self):
        return self.__position

    @classmethod
    def from_string(cls, emp_str):
        name, age, position = emp_str.split("-")
        return cls(name, int(age), position)

    @staticmethod
    def is_valid_age(age):
        return 18 <= age <= 65

    def get_details(self):
        return f"{self.name}, {self.age}, {self.position}"

    def set_address(self, street, city):
        self.address = self.Address(street, city)

    def __str__(self):
        return self.get_details()

    def __repr__(self):
        return f"Employee('{self.name}', {self.age}, '{self.position}')"

    # Nested Class
    class Address:
        def __init__(self, street, city):
            self.street = street
            self.city = city

        def __str__(self):
            return f"{self.street}, {self.city}"

class Manager(Employee):
    def __init__(self, name, age, employees=None):
        super().__init__(name, age, "Manager")
        self.employees = employees if employees else []

    def get_details(self):
        return f"{super().get_details()} - manages {len(self.employees)} employee(s)"
